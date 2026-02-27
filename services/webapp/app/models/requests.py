
from sqlmodel import SQLModel

from app.models.client import Assessment, PhysicalExam, ToddlerExam
from app.models.base import RatingEnum

class AssessmentRequest(SQLModel):
    assessment: Assessment
    medical_history: list["str"] | None = None
    physical_exam: PhysicalExam | None = None
    toddler_exam: ToddlerExam | None = None

class AssessmentFeedbackComment(SQLModel):
    feedback_comment: str
    feedback_rating: RatingEnum | None = None