from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('churn_model.pkl')

from pydantic import BaseModel

class churnInput(BaseModel):
    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

@app.post('/predict')
async def predit(data: churnInput):
    input_data = np.array([[v for v in data.dict().values()]])
    prediction =  model.predict(input_data)
    return {'churn': int(prediction[0])}