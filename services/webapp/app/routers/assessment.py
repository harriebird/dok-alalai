import uuid

from fastapi import APIRouter, HTTPException, Query, Depends, BackgroundTasks
from sqlmodel import Session, select, col

from app.core.llm import analyze_assessment
from app.models import engine, get_session
from app.models.client import Assessment, MedicalCondition
from app.models.responses import AssessmentListInfo, AssessmentFullInfo

assessment_router = APIRouter()


@assessment_router.get("/assessments", response_model=list[AssessmentListInfo])
async def get_assessments(
        offset: int = 0, limit: int = Query(default=100, le=100),
        session: Session = Depends(get_session)):
    assessments = session.exec(select(Assessment).offset(offset).limit(limit)).all()
    return assessments

@assessment_router.get("/assessments/{assessment_uuid}", response_model=AssessmentFullInfo)
async def get_assessment(assessment_uuid: uuid.UUID, session: Session = Depends(get_session)):
    assessment = session.exec(select(Assessment).where(Assessment.uuid == assessment_uuid)).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Client not found")
    return assessment

@assessment_router.get("/assessments/{assessment_uuid}/analyze")
async def assessment_analysis(assessment_uuid: uuid.UUID, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    assessment = session.exec(select(Assessment).where(Assessment.uuid == assessment_uuid)).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Client not found")

    background_tasks.add_task(analyze_assessment, assessment.uuid)

    return {"message": f"Analyzing {assessment_uuid}"}

@assessment_router.post("/conditions")
async def new_condition(medical_condition: MedicalCondition):
    with Session(engine) as session:
        session.add(medical_condition)
        session.commit()
        session.refresh(medical_condition)
        return medical_condition

@assessment_router.get("/conditions/search", response_model=list[MedicalCondition])
async def condition_search(keyword: str, session: Session = Depends(get_session)):
    results = session.exec(select(MedicalCondition).where(MedicalCondition.name.icontains(keyword))).all()
    return results
