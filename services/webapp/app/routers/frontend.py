import uuid

from fastapi import APIRouter, Request

from app.core.config import templates
frontend_router = APIRouter()

@frontend_router.get("/", name="home")
async def index(request: Request):
    return templates.TemplateResponse(request, "pages/index.html")

@frontend_router.get("/clients", name="client-list")
async def clients_page(request: Request):
    return templates.TemplateResponse(request, "pages/client-list.html")

@frontend_router.get("/clients/add", name="client-add")
async def clients_page(request: Request):
    return templates.TemplateResponse(request, "pages/client-add.html")

@frontend_router.get("/clients/{client_uuid}", name="client-info")
async def clients_page(client_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse(request, "pages/client-info.html", {"client_uuid": client_uuid})

@frontend_router.get("/clients/{client_uuid}/assess", name="client-assess")
async def clients_page(client_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse(request, "pages/client-assess-info.html", {"client_uuid": client_uuid})

@frontend_router.get("/ai-feedback", name="feedback-list")
async def clients_page(request: Request):
    return templates.TemplateResponse(request, "pages/feedback-list.html")

@frontend_router.get("/ai-feedback/{feedback_uuid}", name="feedback-info")
async def clients_page(feedback_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse(request, "pages/feedback-info.html", {"feedback_uuid": feedback_uuid})


@frontend_router.get("/assessments", name="assess-list")
async def clients_page(request: Request):
    return templates.TemplateResponse(request, "pages/assess-list.html")

@frontend_router.get("/assessments/{assessment_uuid}", name="assess-info")
async def clients_page(assessment_uuid: uuid.UUID, request: Request):
    return templates.TemplateResponse(request, "pages/assess-info.html", {"assessment_uuid": assessment_uuid})
