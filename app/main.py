from fastapi import FastAPI
from app.db.db import engine
from app.db.base import Base
from app.core.config import settings
from app.routers import (
    known_text_question,
    known_numeric_question,
    user,
    survey,
    numeric_question,
    text_question,
)
from fastapi.responses import RedirectResponse

settings = settings.Settings()

Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(user.router)
app.include_router(survey.router)
app.include_router(numeric_question.router)
app.include_router(text_question.router)
app.include_router(known_text_question.router)
app.include_router(known_numeric_question.router)


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
