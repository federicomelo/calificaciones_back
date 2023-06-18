from sqlalchemy.orm import Session
from app.db.base import KnownNumericQuestion as KnownNumericQuestionModel
from app.db.schemas.known_numeric_question import (
    KnownNumericQuestion,
    KnownNumericQuestionCreate,
)
from typing import List


def get_known_numeric_question(db: Session, id: int):
    return (
        db.query(KnownNumericQuestionModel)
        .filter(KnownNumericQuestionModel.id == id)
        .first()
    )


def get_known_numeric_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(KnownNumericQuestionModel).offset(skip).limit(limit).all()


def create_known_numeric_question(
    db: Session, known_numeric_question: KnownNumericQuestionCreate
):
    db_known_numeric_question = KnownNumericQuestionModel(
        question=known_numeric_question.question,
        is_optional=known_numeric_question.is_optional,
    )
    db.add(db_known_numeric_question)
    db.commit()
    db.refresh(db_known_numeric_question)
    return db_known_numeric_question


def create_known_numeric_questions(
    db: Session, known_numeric_questions: List[KnownNumericQuestionCreate]
):
    db_known_numeric_questions = []
    for known_numeric_question in known_numeric_questions:
        db_known_numeric_question = KnownNumericQuestionModel(
            question=known_numeric_question.question,
            is_optional=known_numeric_question.is_optional,
        )
        db.add(db_known_numeric_question)
        db_known_numeric_questions.append(db_known_numeric_question)
    db.commit()
    return db_known_numeric_questions


def update_known_numeric_question(
    db: Session, id: int, known_numeric_question: KnownNumericQuestion
):
    db_known_numeric_question = (
        db.query(KnownNumericQuestionModel)
        .filter(KnownNumericQuestionModel.id == id)
        .first()
    )
    db_known_numeric_question.question = known_numeric_question.question
    db.commit()
    db.refresh(db_known_numeric_question)
    return db_known_numeric_question


def delete_known_numeric_question(db: Session, id: int):
    rows_deleted = (
        db.query(KnownNumericQuestionModel)
        .filter(KnownNumericQuestionModel.id == id)
        .delete()
    )
    db.commit()
    return rows_deleted
