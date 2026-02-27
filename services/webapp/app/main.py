from fastapi import FastAPI, File, UploadFile, HTTPException, status, APIRouter
from fastapi.responses import StreamingResponse

from starlette.staticfiles import StaticFiles

from app.routers import router
from app.core import llm
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)


@app.post("/analyze-image")
async def check_image(file: UploadFile):
    if not file.content_type.startswith("image"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only png, jpeg, gif and png are accepted"
        )

    return StreamingResponse(llm.analyze_image(file))
