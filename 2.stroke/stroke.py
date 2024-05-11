import os
import joblib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from stroke_models import PatientBatch, Patient

FEATURES = [
    'age',
    'hypertension',
    'heart_disease',
    'avg_glucose_level',
    'bmi',
    'gender_Female',
    'gender_Male',
    'gender_Other',
    'ever_married_No',
    'ever_married_Yes',
    'work_type_Govt_job',
    'work_type_Never_worked',
    'work_type_Private',
    'work_type_Self-employed',
    'work_type_children',
    'Residence_type_Rural',
    'Residence_type_Urban',
    'smoking_status_Unknown',
    'smoking_status_formerly smoked',
    'smoking_status_never smoked',
    'smoking_status_smokes',
    ]

class StrokeModel:
    def __init__(self, model_path: str | None = None):
        self.model: DecisionTreeClassifier = joblib.load(model_path) if model_path is not None else DecisionTreeClassifier()
        self.features = FEATURES

    def preprocess_patients(self, patients: list[dict]):
        # read as dataframe
        df = pd.DataFrame(patients)
        
        # convert to one hot encoding
        input_df = pd.get_dummies(df, columns=["gender", "ever_married", "work_type", "Residence_type", "smoking_status"])
        # complete features
        for col in self.features:
            if col not in input_df.columns:
                input_df[col] = 0
        # reorder features
        input_ids = input_df["id"].values.tolist()
        input_df = input_df.drop(columns=["id"])
        input_df = input_df[self.features]
        return input_df, input_ids

    def preprocess_patient_batch(self, patient_batch: PatientBatch):
        # extract as dictionary
        batch_dict = patient_batch.model_dump(by_alias=True)
        patients = batch_dict["patients"]
        return self.preprocess_patients(patients)
    
    def preprocess_patient(self, patient: Patient):

        return self.preprocess_patients([patient.model_dump(by_alias=True)])

    def predict_batch(self, patient_batch: PatientBatch):
        inputs, ids = self.preprocess_patient_batch(patient_batch)
        prediction = self.model.predict(inputs).tolist()
        return prediction, ids
    
    def predict_single(self, patient: Patient):
        inputs, ids = self.preprocess_patient(patient)
        prediction = self.model.predict(inputs).tolist()
        return prediction, ids
    