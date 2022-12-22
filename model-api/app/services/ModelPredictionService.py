
from schemas.ModelSchema import ModelSchema


class ModelPredictionService:
    def get_prediction(self, model: ModelSchema, input: dict, model_categories: list):
        try:
            print("ok ModelPredictService " )
            response=model.predict(input, model_categories)
            print("ok model.predict" ) 
            print(response )                       
            return { "probability of a flight delay": str(response[0])}
        except:
            return None