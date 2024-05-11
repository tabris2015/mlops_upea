from datetime import datetime
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from stroke_models import Patient, PatientBatch, PatientPrediction, BatchResponse
from stroke import StrokeModel

MODEL_PATH = "model.joblib"

app = FastAPI(title="Stroke API")

def get_stroke_model():
    return StrokeModel(model_path=MODEL_PATH)


@app.post("/stroke/predict")
def predict_patients(patient_batch: PatientBatch, model: StrokeModel = Depends(get_stroke_model)):
    preds, ids = model.predict_batch(patient_batch)
    predictions = [PatientPrediction(id=id, pred=pred) for id, pred in zip(ids, preds)]
    return BatchResponse(predictions=predictions)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("prediction_api:app", reload=True)