import uuid

from fastapi import APIRouter, Request

from app.core.config import templates
frontend_router = APIRouter()

@frontend_router.get("/", name="home")
async def index(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@frontend_router.get("/clients", name="client-list")
async def clients_page(request: Request):
    return templates.TemplateResponse("pages/client-list.html", {"request": request})

@frontend_router.get("/clients/add", name="client-add")
async def clients_page(request: Request):
    return templates.TemplateResponse("pages/client-add.html", {"request": request})

@frontend_router.get("/clients/{client_uuid}", name="client-info")
async def clients_page(client_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse("pages/client-info.html", {"request": request, "client_uuid": client_uuid })

@frontend_router.get("/clients/{client_uuid}/assess", name="client-assess")
async def clients_page(client_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse("pages/client-assess-info.html", {"request": request, "client_uuid": client_uuid })

@frontend_router.get("/ai-feedback", name="feedback-list")
async def clients_page(request: Request):
    return templates.TemplateResponse("pages/feedback-list.html", {"request": request})

@frontend_router.get("/ai-feedback/{feedback_uuid}", name="feedback-info")
async def clients_page(feedback_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse("pages/feedback-info.html", {"request": request, "feedback_uuid": feedback_uuid })


@frontend_router.get("/assessments", name="assess-list")
async def clients_page(request: Request):
    return templates.TemplateResponse("pages/assess-list.html", {"request": request })

@frontend_router.get("/assessments/{assessment_uuid}", name="assess-info")
async def clients_page(assessment_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse("pages/assess-info.html", {"request": request, "assessment_uuid": assessment_uuid })
