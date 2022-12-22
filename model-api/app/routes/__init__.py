from fastapi import APIRouter
from app.routes.model_predict_routers import modelPredictRouter


router = APIRouter()
router.include_router(modelPredictRouter, prefix="/predictAtrasos")


__all__ = ["router"]