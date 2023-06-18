from fastapi import FastAPI
from app.db.db import engine
from app.db.base import Base
from app.core.config import settings
from app.routers import (
    assignment,
    semester,
    subject,
)
from fastapi.responses import RedirectResponse

settings = settings.Settings()

Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(assignment.router)
app.include_router(semester.router)
app.include_router(subject.router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
