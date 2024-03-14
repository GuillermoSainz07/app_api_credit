from fastapi import APIRouter
from schemas.features import Features
from config_db.database import Session
from services.prediction import ModelPrediction
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder



pred_route = APIRouter()

@pred_route.post('/predict_model', tags=['Prediction'], response_model=dict)
def make_prediction(features:Features) -> dict:
    db = Session()
    result = ModelPrediction(db, features.model_name).make_prediction(**features.model_dump())
    result_str = 'Default' if int(result) == 1 else "Non Default"
    return JSONResponse(content={'Prediction': str(result_str)})








    
