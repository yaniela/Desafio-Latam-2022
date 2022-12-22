from fastapi import APIRouter
from app.controller.ModelPredictController  import ModelPredictController
#from source.Models import Models
from schemas.ItemSchema import ItemSchema
from schemas.ModelSchema import ModelSchema
from utils import converter
import pickle
import shutil

with open ('models/categories', 'rb') as fp:
    model_categories = pickle.load(fp)

modelPredictRouter = APIRouter()
modelPredictController = ModelPredictController()
model=ModelSchema("'models/model_version_1_0_0.joblib'")



@modelPredictRouter.get('/')
async def test():
    return {'Test': 'Predict probability of flight delay test'}


@modelPredictRouter.post("/predict")
async def get_prediction(item: ItemSchema):
    return modelPredictController.get_prediction(model, item, model_categories)



__all__ = ["modelPredictRouter"]