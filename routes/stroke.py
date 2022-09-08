import os
import pickle
from google.cloud import storage
from fastapi import APIRouter, Body
from pydantic import BaseModel, Field
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier

router = APIRouter()
#Get Environment Variables
PROJECT=os.getenv("PROJECT")
STORAGE_BUCKET=os.getenv("BUCKET_NAME")

class StrokeParameters(BaseModel):

    have_heart_disease: str = Field(..., title="Heart Disease?",
    desceription="Does patient have disease?")

    ever_smoked: str = Field(..., title="smoker",
    description="Does patitients smoke")

    have_hypertention: str = Field(..., title="Hypertention",
    description="Does patients have hypertention")

    glucose: float = Field(..., title="Average glucose level",
    description="Patient glucose level")

    bmi: float = Field(..., title="Body maths Index",
    description="Patient body maths index")

@router.post("/stroke")
async def predictStroke(stroke: StrokeParameters = Body(...)):

    if stroke.ever_smoked == "formerly smoked":
        formaly_smoke = 1.0
        never_smoke = 0.0
        unknown = 0.0
        smokes = 0.0

    elif stroke.ever_smoked == "never smoked":
        formaly_smoke = 0.0
        never_smoke = 1.0
        unknown = 0.0
        smokes = 0.0

    elif stroke.ever_smoked == "smokes":
        formaly_smoke = 0.0
        never_smoke = 0.0
        unknown = 0.0
        smokes = 1.0

    else:
        formaly_smoke = 0.0
        never_smoke = 0.0
        unknown = 1.0
        smokes = 0.0
    

    if stroke.have_hypertention == "yes":
        have_hypertention = 1
    else:
        have_hypertention = 0


    if stroke.have_heart_disease == "yes":
        have_heart_disease = 1.0
    else:
        have_heart_disease = 0.0

    # Scale Bmi and Glucose Level
    robust_scaler = RobustScaler()

    # Fit and transform on dataset
    bmi_glucose = robust_scaler.fit_transform([[stroke.bmi, stroke.glucose]])

    #Gety scaled values
    bmi = bmi_glucose[0][0]
    glucose = bmi_glucose[0][1]

    #Get final imput data
    input = [
        unknown, 
        formaly_smoke, 
        never_smoke, 
        smokes, 
        glucose, 
        have_hypertention, 
        have_heart_disease, 
        bmi
    ]

    # Configure storage account
    client = storage.Client(project=PROJECT)
    bucket = client.get_bucket(STORAGE_BUCKET)

    # Refrence model.pkl file in storage account
    blob = bucket.blob("model.pkl")

    #Download model in temporary directory
    blob.download_to_filename("/tmp/model.pkl")

    # Load model from temporary directory
    saved_model = pickle.load(open("/tmp/model.pkl","rb"))

    # Make prediction using model
    predicted = saved_model.predict([input])

    # Return responds after prediction
    if predicted[0] == 1:
        return {"Predicted": "Stroke Patient"}
        
    else:
        return {"Predicted": "Not A Stroke Patient"}