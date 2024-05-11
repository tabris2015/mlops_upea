from datetime import datetime
from pydantic import BaseModel, Field


class Patient(BaseModel):
    id: int
    gender: str
    age: int
    hypertension: bool
    heart_disease: bool
    ever_married: str
    work_type: str
    residence_type: str = Field(alias="Residence_type")
    avg_glucose_level: float
    bmi: float
    smoking_status: str

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
