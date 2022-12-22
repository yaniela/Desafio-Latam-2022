
from app.services.ModelPredictionService import ModelPredictionService
from schemas import ItemSchema, ModelSchema
from utils import converter


modelPredictionService= ModelPredictionService()


class ModelPredictController:

    def get_prediction(self,model:ModelSchema, item:ItemSchema, model_categories:list ):  
          print("ok ModelPredictController" )

          input=converter.convert_itemschema_to_dict(item)

          print("ok ModelPredictController antes de pasara a service" )
          return modelPredictionService.get_prediction(model, input, model_categories)

     
         
         


__all__ = ['ImageClassifierController']