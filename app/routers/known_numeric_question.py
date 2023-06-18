from app.logic import known_numeric_question as logic
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import known_numeric_question as schema

router = APIRouter(
    prefix="/known_numeric_questions",
    tags=["known_numeric_questions"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.KnownNumericQuestion])
def get_known_numeric_questions(db: Session = Depends(get_db)):
    known_numeric_questions = logic.get_known_numeric_questions(db)
    return known_numeric_questions


@router.get("/{id}", response_model=schema.KnownNumericQuestion)
def get_known_numeric_question(id: int, db: Session = Depends(get_db)):
    db_known_numeric_question = logic.get_known_numeric_question(db, id=id)
    if db_known_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return db_known_numeric_question


@router.post("/", response_model=schema.KnownNumericQuestion)
def create_known_numeric_question(
    known_numeric_question: schema.KnownNumericQuestion, db: Session = Depends(get_db)
):
    return logic.create_known_numeric_question(
        db=db, known_numeric_question=known_numeric_question
    )


@router.post("/many", response_model=List[schema.KnownNumericQuestion])
def create_known_numeric_questions(
    known_numeric_questions: List[schema.KnownNumericQuestion],
    db: Session = Depends(get_db),
):
    return logic.create_known_numeric_questions(
        db=db, known_numeric_questions=known_numeric_questions
    )


@router.put("/{id}", response_model=schema.KnownNumericQuestion)
def update_known_numeric_question(
    id: int,
    known_numeric_question: schema.KnownNumericQuestionCreate,
    db: Session = Depends(get_db),
):
    db_known_numeric_question = logic.get_known_numeric_question(db, id=id)
    if db_known_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return logic.update_known_numeric_question(
        db=db, id=id, known_numeric_question=known_numeric_question
    )


@router.delete("/{id}")
def delete_known_numeric_question(id: int, db: Session = Depends(get_db)):
    db_known_numeric_question = logic.get_known_numeric_question(db, id=id)
    if db_known_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Known text question with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_known_numeric_question(db=db, id=id)} known_numeric_question"
    }
