from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    albuminuria: float
    creatinine: float
    eGFR: float
    uric_acid: float