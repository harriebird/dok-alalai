import uuid
from datetime import datetime

from sqlmodel import SQLModel

from app.models.base import AssessmentBase, ClientBase, RatingEnum
from app.models.client import MedicalCondition, ToddlerExam, PhysicalExam, AssessmentFeedback

class ClientQuickInfo(SQLModel):
    uuid: uuid.UUID
    first_name: str
    middle_name: str
    last_name: str
    ext_name: str

class ClientListInfo(SQLModel):
    uuid: uuid.UUID
    first_name: str
    middle_name: str
    last_name: str
    ext_name: str
    birth_date: datetime
    sex: str
    civil_status: str
    contact_number: str

class AssessmentFullInfo(AssessmentBase):
    client : ClientBase | None = None
    medical_history : list["MedicalCondition"] | None = None
    physical_exam: PhysicalExam | None
    toddler_exam: ToddlerExam | None
    feedback: list["AssessmentFeedbackQuickInfo"] | None = None

class AssessmentFeedbackQuickInfo(SQLModel):
    id : int
    uuid: uuid.UUID
    created_at: datetime
    generate_duration: float | None = None
    feedback_rating: RatingEnum | None = None

class AssessmentListInfo(SQLModel):
    id: int
    uuid: uuid.UUID
    client: ClientQuickInfo
    feedback: list["AssessmentFeedbackQuickInfo"]
    created_at: datetime
    updated_at: datetime | None

class AssessmentQuickInfo(SQLModel):
    id: int
    uuid: uuid.UUID
    client: ClientQuickInfo
    created_at: datetime
    updated_at: datetime | None

class AssessmentFeedbackListInfo(SQLModel):
    id: int
    uuid: uuid.UUID
    assessment: AssessmentQuickInfo
    feedback_rating: RatingEnum | None = None
    created_at: datetime
    generate_duration: float | None = None
    commented : bool

class AssessmentFeedbackFullInfo(SQLModel):
    id: int
    uuid: uuid.UUID
    assessment: AssessmentQuickInfo
    ai_feedback: str
    feedback_rating: RatingEnum | None = None
    feedback_comment: str | None
    created_at: datetime
    updated_at: datetime | None
    commented: bool
