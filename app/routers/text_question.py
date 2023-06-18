from app.logic import text_question as logic
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import text_question as schema

router = APIRouter(
    prefix="/text_questions",
    tags=["text_questions"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.TextQuestion])
def get_text_questions(db: Session = Depends(get_db)):
    text_questions = logic.get_text_questions(db)
    return text_questions


@router.get("/{id}", response_model=schema.TextQuestion)
def get_text_question(id: int, db: Session = Depends(get_db)):
    db_text_question = logic.get_text_question(db, id=id)
    if db_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Text question with id {id} not found"
        )
    return db_text_question


@router.post("/", response_model=schema.TextQuestion)
def create_text_question(
    TextQuestion: schema.TextQuestion, db: Session = Depends(get_db)
):
    return logic.create_text_question(db=db, text_question=TextQuestion)


@router.put("/{id}", response_model=schema.TextQuestion)
def update_text_question(
    id: int,
    text_question_schema: schema.TextQuestionCreate,
    db: Session = Depends(get_db),
):
    db_text_question = logic.get_text_question(db, id=id)
    if db_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Text question with id {id} not found"
        )
    return logic.update_text_question(db=db, id=id, text_question=text_question_schema)


@router.delete("/{id}")
def delete_text_question(id: int, db: Session = Depends(get_db)):
    db_text_question = logic.get_text_question(db, id=id)
    if db_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Text question with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_text_question(db=db, id=id)} text_question"
    }
