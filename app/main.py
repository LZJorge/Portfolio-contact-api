from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.routes.v1.router import router
from app.config.settings import settings


app = FastAPI()
app.include_router(router)


@app.get("/ping", tags=["Health"], status_code=200)
async def root():
    return {"message": "pong"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.app_url],
    allow_methods=["GET", "POST"],
    allow_headers=["Accept", "Content-Type", "X-KEY"],
)
