from fastapi import FastAPI, File, UploadFile, HTTPException, status, APIRouter
from fastapi.responses import StreamingResponse

from starlette.staticfiles import StaticFiles

from app.routers import router
from app.core import llm
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)
