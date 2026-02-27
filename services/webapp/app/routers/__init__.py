from fastapi import APIRouter

from app.routers.assessment import assessment_router
from app.routers.client import client_router
from app.routers.feedback import feedback_router
from app.routers.frontend import frontend_router


router = APIRouter()
api_router = APIRouter(prefix="/api")
api_router.include_router(assessment_router)
api_router.include_router(client_router)
api_router.include_router(feedback_router)
router.include_router(frontend_router)
router.include_router(api_router)