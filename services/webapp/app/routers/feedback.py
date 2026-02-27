import uuid
from datetime import datetime

from fastapi import APIRouter, HTTPException, Query, Depends
from sqlmodel import Session, select

from app.models import get_session
from app.models.responses import AssessmentFeedbackListInfo, AssessmentFeedbackFullInfo
from app.models.requests import AssessmentFeedbackComment
from app.models.client import AssessmentFeedback

feedback_router = APIRouter()

@feedback_router.get("/ai-feedback", response_model=list[AssessmentFeedbackListInfo])
async def get_assessments(
        offset: int = 0, limit: int = Query(default=100, le=100),
        session: Session = Depends(get_session)):
    feedbacks = session.exec(select(AssessmentFeedback).offset(offset).limit(limit)).all()
    return feedbacks

@feedback_router.get("/ai-feedback/{feedback_uuid}", response_model=AssessmentFeedbackFullInfo)
async def get_client(feedback_uuid: uuid.UUID, session: Session = Depends(get_session)):
    feedback = session.exec(select(AssessmentFeedback).where(AssessmentFeedback.uuid == feedback_uuid)).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Client not found")
    return feedback

@feedback_router.patch("/ai-feedback/{feedback_uuid}/comment")
async def get_client(feedback_uuid: uuid.UUID, comment: AssessmentFeedbackComment, session: Session = Depends(get_session)):
    feedback = session.exec(select(AssessmentFeedback).where(AssessmentFeedback.uuid == feedback_uuid)).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Client not found")
    feedback_comment = comment.model_dump(exclude_unset=True)
    feedback.sqlmodel_update(feedback_comment)
    feedback.updated_at = datetime.now()
    session.add(feedback)
    session.commit()
    session.refresh(feedback)
    return feedback