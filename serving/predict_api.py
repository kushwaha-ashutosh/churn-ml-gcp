from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("artifacts/model.joblib")


class CustomerFeatures(BaseModel):
    avg_usage_30d: float
    login_frequency_30d: float
    support_tickets_60d: int


@app.post("/predict")
def predict(features: CustomerFeatures):
    data = [[
        features.avg_usage_30d,
        features.login_frequency_30d,
        features.support_tickets_60d
    ]]

    prob = model.predict_proba(data)[0][1]

    return {
        "churn_probability": float(prob),
        "risk_level": "HIGH" if prob > 0.7 else "LOW"
    }
