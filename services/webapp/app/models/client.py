from sqlmodel import Field, Relationship

from app.models.base import (BaseModel, LinkModel, AssessmentBase,
                             ClientBase, PhysicalExamBase,
                             ToddlerExamBase, AssessmentFeedbackBase)

class EncounterCondition(LinkModel, table=True):
    assessment_id : int | None = Field(default=None, foreign_key="assessment.id")
    condition_id : int | None = Field(default=None, foreign_key="medicalcondition.id")

class MedicalCondition(BaseModel, table=True):
    name: str = Field(max_length=50)
    assessments : list["Assessment"] = Relationship(
        back_populates="medical_history", link_model=EncounterCondition
    )

class Client(ClientBase, BaseModel, table=True):
    assessments: list["Assessment"] = Relationship(back_populates="client")

class PhysicalExam(PhysicalExamBase, BaseModel, table=True):
    assessment : Assessment = Relationship(back_populates="physical_exam")

class ToddlerExam(ToddlerExamBase, BaseModel, table=True):
    assessment: Assessment = Relationship(back_populates="toddler_exam")

class Assessment(AssessmentBase, BaseModel, table=True):
    client: Client = Relationship(back_populates="assessments")
    medical_history: list["MedicalCondition"] = Relationship(
        back_populates="assessments", link_model=EncounterCondition
    )
    physical_exam : PhysicalExam = Relationship(
        back_populates="assessment", sa_relationship_kwargs={"uselist": False}
    )
    toddler_exam : ToddlerExam | None = Relationship(
        back_populates="assessment", sa_relationship_kwargs={"uselist": False}
    )
    feedback : list["AssessmentFeedback"] = Relationship(back_populates="assessment")

class AssessmentFeedback(AssessmentFeedbackBase, BaseModel, table=True):
    assessment : Assessment = Relationship(back_populates="feedback")
