from schemas.features import Features
import joblib
import numpy as np
from tables.pred_table import PredTable

class ModelPrediction:
    def __init__(self, db, model_name) -> None:
        self.db = db # Session Data Baseb
        self.model_name = model_name
    def make_prediction(self,**kwargs):
        if self.model_name == "RandomForest":
            model = joblib.load("models/RForestModel.pkl")
        else:
            model = joblib.load("models/XGBoostModel.pkl")


        features = [value for key,value in kwargs.items() if key!="model_name"]
        features = np.array(features).reshape(1,-1)
        predict = model.predict(features)[0]
        predict_string = 'Default' if predict == 1 else "Non Default"
        new_movie = PredTable(**kwargs)

        new_movie.prediction = predict_string
        self.db.add(new_movie)
        self.db.commit()

        return predict
    

    




