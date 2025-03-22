from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the expected data structure
class SensorData(BaseModel):
    albuminuria: float
    creatinine: float
    eGFR: float
    uric_acid: float

@app.post("/upload-data/")
def upload_data(data: SensorData):
    return {"message": "Data received", "data": data}
