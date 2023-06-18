from app.logic import known_text_question as logic
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import known_text_question as schema

router = APIRouter(
    prefix="/known_text_questions",
    tags=["known_text_questions"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.KnownTextQuestion])
def get_known_text_questions(db: Session = Depends(get_db)):
    known_text_questions = logic.get_known_text_questions(db)
    return known_text_questions


@router.get("/{id}", response_model=schema.KnownTextQuestion)
def get_known_text_question(id: int, db: Session = Depends(get_db)):
    db_known_text_question = logic.get_known_text_question(db, id=id)
    if db_known_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return db_known_text_question


@router.post("/", response_model=schema.KnownTextQuestion)
def create_known_text_question(
    known_text_question: schema.KnownTextQuestion, db: Session = Depends(get_db)
):
    return logic.create_known_text_question(
        db=db, known_text_question=known_text_question
    )


@router.post("/many", response_model=List[schema.KnownTextQuestion])
def create_known_text_questions(
    known_text_questions: List[schema.KnownTextQuestion],
    db: Session = Depends(get_db),
):
    return logic.create_known_text_questions(
        db=db, known_text_questions=known_text_questions
    )


@router.put("/{id}", response_model=schema.KnownTextQuestion)
def update_known_text_question(
    id: int,
    known_text_question: schema.KnownTextQuestionCreate,
    db: Session = Depends(get_db),
):
    db_known_text_question = logic.get_known_text_question(db, id=id)
    if db_known_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return logic.update_known_text_question(
        db=db, id=id, known_text_question=known_text_question
    )


@router.delete("/{id}")
def delete_known_text_question(id: int, db: Session = Depends(get_db)):
    db_known_text_question = logic.get_known_text_question(db, id=id)
    if db_known_text_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_known_text_question(db=db, id=id)} known_text_question"
    }
