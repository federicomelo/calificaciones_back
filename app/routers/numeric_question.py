from app.logic import numeric_question as logic
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import numeric_question as schema

router = APIRouter(
    prefix="/numeric_questions",
    tags=["numeric_questions"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.NumericQuestion])
def get_numeric_questions(db: Session = Depends(get_db)):
    numeric_questions = logic.get_numeric_questions(db)
    return numeric_questions


@router.get("/{id}", response_model=schema.NumericQuestion)
def get_numeric_question(id: int, db: Session = Depends(get_db)):
    db_numeric_question = logic.get_numeric_question(db, id=id)
    if db_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Numeric question with id {id} not found"
        )
    return db_numeric_question


@router.post("/", response_model=schema.NumericQuestion)
def create_numeric_question(
    NumericQuestion: schema.NumericQuestion, db: Session = Depends(get_db)
):
    return logic.create_numeric_question(db=db, numeric_question=NumericQuestion)


@router.put("/{id}", response_model=schema.NumericQuestion)
def update_numeric_question(
    id: int,
    numeric_question_schema: schema.NumericQuestionCreate,
    db: Session = Depends(get_db),
):
    db_numeric_question = logic.get_numeric_question(db, id=id)
    if db_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Numeric question with id {id} not found"
        )
    return logic.update_numeric_question(
        db=db, id=id, numeric_question=numeric_question_schema
    )


@router.delete("/{id}")
def delete_numeric_question(id: int, db: Session = Depends(get_db)):
    db_numeric_question = logic.get_numeric_question(db, id=id)
    if db_numeric_question is None:
        raise HTTPException(
            status_code=404, detail=f"Numeric question with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_numeric_question(db=db, id=id)} numeric_question"
    }
