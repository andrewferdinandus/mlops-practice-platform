from pathlib import Path
import json

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "model.joblib"
FEATURES_PATH = BASE_DIR / "models" / "feature_names.json"


app = FastAPI(
    title="MLOps Lab 03 - FastAPI Model Serving",
    description="A simple API that serves a trained ML model for predictions.",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    age: float = Field(..., example=0.0380759064334241)
    sex: float = Field(..., example=0.0506801187398186)
    bmi: float = Field(..., example=0.0616962065186885)
    bp: float = Field(..., example=0.0218723855140367)
    s1: float = Field(..., example=-0.0442234984244464)
    s2: float = Field(..., example=-0.0348207628376986)
    s3: float = Field(..., example=-0.0434008456520269)
    s4: float = Field(..., example=-0.00259226199818328)
    s5: float = Field(..., example=0.0199074861704627)
    s6: float = Field(..., example=-0.0176461251598038)


class PredictionResponse(BaseModel):
    prediction: float
    model_name: str
    mlops_stage: str


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}. "
            "Run python src/train_model.py first."
        )

    if not FEATURES_PATH.exists():
        raise FileNotFoundError(
            f"Feature names file not found: {FEATURES_PATH}. "
            "Run python src/train_model.py first."
        )

    model = joblib.load(MODEL_PATH)

    with FEATURES_PATH.open("r", encoding="utf-8") as file:
        feature_names = json.load(file)

    return model, feature_names


model, feature_names = load_model()


@app.get("/")
def root():
    return {
        "message": "MLOps Lab 03 FastAPI Model Serving",
        "docs": "/docs",
        "health": "/health",
        "predict": "/predict"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "feature_count": len(feature_names)
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    input_data = pd.DataFrame(
        [[
            request.age,
            request.sex,
            request.bmi,
            request.bp,
            request.s1,
            request.s2,
            request.s3,
            request.s4,
            request.s5,
            request.s6
        ]],
        columns=feature_names
    )

    prediction = model.predict(input_data)[0]

    return PredictionResponse(
        prediction=float(prediction),
        model_name="Ridge Regression",
        mlops_stage="model serving"
    )
