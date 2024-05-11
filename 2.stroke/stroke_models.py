from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class EverMarriedType(str, Enum):
    yes = "Yes"
    no = "No"

class WorkType(str, Enum):
    govt_job = "Govt_job"
    never_worked = "Never_worked"
    private = "Private"
    self_employed = "Self-employed"
    children = "children"

class ResidenceType(str, Enum):
    rural = "Rural"
    urban = "Urban"

class SmokingStatus(str, Enum):
    unknown = "Unknown"
    formerly_smoked = "formerly smoked"
    never_smoked = "never smoked"
    smokes = "smokes"

class Patient(BaseModel):
    id: int
    gender: str
    age: int
    hypertension: bool
    heart_disease: bool
    ever_married: EverMarriedType
    work_type: WorkType
    residence_type: ResidenceType = Field(alias="Residence_type")
    avg_glucose_level: float
    bmi: float
    smoking_status: SmokingStatus

class PatientBatch(BaseModel):
    hospital: str
    city: str
    sent_at: datetime
    patients: list[Patient]

class PatientPrediction(BaseModel):
    id: int
    pred: int

class BatchResponse(BaseModel):
    predictions: list[PatientPrediction]
