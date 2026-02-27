import uuid
from datetime import datetime, date
from enum import Enum

from sqlmodel import SQLModel, Field


class GenSurveyEnum(str, Enum):
    AWAKE = "Awake and alert"
    ALTERED = "Altered sensorium"

class SexEnum(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class CivilStatusEnum(str, Enum):
    SINGLE = "Single"
    MARRIED = "Married"
    SEPARATED = "Legally Separated"
    WIDOWED = "Widowed"

class BloodTypeEnum(str, Enum):
    APLUS = "A+"
    ABPLUS = "AB+"
    BPLUS = "B+"
    OPLUS = "O+"
    AMINUS = "A-"
    ABMINUS = "AB-"
    BMINUS = "B-"
    OMINUS = "O-"

class RatingEnum(str, Enum):
    STR_DISAGREE = "Strongly Disagree"
    DISAGREE = "Disagree"
    NEUTRAL = "Neutral"
    AGREE = "Agree"
    STR_AGREE = "Strongly Agree"


class BaseModel(SQLModel):
    id : int | None = Field(default=None, primary_key=True, unique=True)
    uuid: uuid.UUID = Field(default_factory=uuid.uuid4, unique=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=None, nullable=True)

class LinkModel(SQLModel):
    id: int | None = Field(primary_key=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.now)

class ClientBase(SQLModel):
    first_name: str = Field(max_length=100)
    middle_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    ext_name: str = Field(max_length=5)
    civil_status: CivilStatusEnum = Field()
    sex: SexEnum = Field()
    email: str = Field()
    contact_number: str = Field(max_length=15)
    philhealth_number: str = Field(max_length=15)
    birth_date: date = Field()

class AssessmentBase(SQLModel):
    client_id: int | None = Field(default=None, foreign_key="client.id")
    question1: str | None = Field()
    question2: str | None = Field()
    question3: str | None = Field()
    question4: str | None = Field()
    question5: str | None = Field()
    question6: str | None = Field()
    question7a: date | None = Field()
    question7b: date | None = Field()
    question7c: int | None = Field()
    question8: str | None = Field()
    smoke_years: float | None = Field(default=None)
    alcohol_years: float | None = Field(default=None)

class PhysicalExamBase(SQLModel):
    assessment_id: int | None = Field(default=None, foreign_key="assessment.id")
    bp_systolic: int | None = Field()
    bp_diastolic: int | None = Field()
    blood_type: BloodTypeEnum | None = Field()
    heart_rate: int | None = Field()
    respiration_rate: int | None = Field()
    va_top: int | None = Field()
    va_bottom: int | None = Field()
    height: float | None = Field()
    weight: float | None = Field()
    temperature: float | None = Field()
    gen_survey: GenSurveyEnum | None = Field()
    additional_notes: str | None = Field()

class ToddlerExamBase(SQLModel):
    assessment_id: int | None = Field(default=None, foreign_key="assessment.id")
    length: float | None = Field()
    body_waist_circ: float | None = Field()
    mid_upper_arm_circ: float | None = Field()
    head_circ: float | None = Field()
    hip: float | None = Field()
    skinfold_thick: float | None = Field()
    limbs: float | None = Field()

class AssessmentFeedbackBase(SQLModel):
    assessment_id: int | None = Field(default=None, foreign_key="assessment.id")
    ai_feedback: str | None = Field(default=None)
    feedback_rating: RatingEnum | None = Field()
    feedback_comment: str | None = Field(default=None)

    @property
    def commented(self) -> bool:
        return self.feedback_comment is not None