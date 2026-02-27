import uuid

from fastapi import APIRouter, HTTPException, Query, BackgroundTasks, Depends
from sqlmodel import Session, select

from app.core.llm import analyze_assessment
from app.models import engine, get_session
from app.models.client import Client, MedicalCondition, EncounterCondition, Assessment
from app.models.requests import AssessmentRequest
from app.models.responses import ClientListInfo, AssessmentListInfo

client_router = APIRouter()

@client_router.get("/clients", response_model=list[ClientListInfo])
async def get_clients(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        clients = session.exec(select(Client).offset(offset).limit(limit)).all()
        return clients

@client_router.get("/clients/{client_uuid}")
async def get_client(client_uuid: uuid.UUID):
    with Session(engine) as session:
        client = session.exec(select(Client).where(Client.uuid == client_uuid)).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
@client_router.post("/clients")
async def create_client(client: Client):
    with Session(engine) as session:
        session.add(client)
        session.commit()
        session.refresh(client)
        return client

@client_router.get("/clients/{client_uuid}/assessments", response_model=list[AssessmentListInfo])
async def get_client_assessments(client_uuid: uuid.UUID, offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_session)):
    client = session.exec(select(Client).where(Client.uuid == client_uuid)).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    assessments = session.exec(select(Assessment)
                               .where(Assessment.client == client).offset(offset).limit(limit)).all()
    return assessments

@client_router.post("/clients/{client_uuid}/assess")
async def new_assessment(client_uuid: uuid.UUID, new_assess_data: AssessmentRequest, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    client = session.exec(select(Client).where(Client.uuid == client_uuid)).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    new_assess = new_assess_data.assessment
    new_assess.client_id = client.id
    session.add(new_assess)
    session.commit()
    session.refresh(new_assess)
    if new_assess_data.medical_history:
        medical_history = new_assess_data.medical_history
        for condition in medical_history:
            medical_condition = session.exec(select(MedicalCondition)
                                             .where(MedicalCondition.name == condition)).first()
            if medical_condition:
                new_medical_history = EncounterCondition()
                new_medical_history.assessment_id = new_assess.id
                new_medical_history.condition_id = medical_condition.id
                session.add(new_medical_history)
                session.commit()
            else:
                to_add_condition = MedicalCondition()
                to_add_condition.name = condition
                session.add(to_add_condition)
                session.commit()
                session.refresh(to_add_condition)

                new_medical_history = EncounterCondition()
                new_medical_history.assessment_id = new_assess.id
                new_medical_history.condition_id = to_add_condition.id
                session.add(new_medical_history)
                session.commit()

    if new_assess_data.physical_exam:
        physical_exam = new_assess_data.physical_exam
        physical_exam.assessment_id = new_assess.id
        session.add(physical_exam)
        session.commit()

    if new_assess_data.toddler_exam:
        toddler_exam = new_assess_data.toddler_exam
        toddler_exam.assessment_id = new_assess.id
        session.add(toddler_exam)
        session.commit()

    background_tasks.add_task(analyze_assessment, new_assess.uuid)

    return new_assess
