from sqlalchemy.orm import Session
from app.db.base import KnownTextQuestion as KnownTextQuestionModel
from app.db.schemas.known_text_question import (
    KnownTextQuestion,
    KnownTextQuestionCreate,
)
from typing import List


def get_known_text_question(db: Session, id: int):
    return (
        db.query(KnownTextQuestionModel).filter(KnownTextQuestionModel.id == id).first()
    )


def get_known_text_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(KnownTextQuestionModel).offset(skip).limit(limit).all()


def create_known_text_question(
    db: Session, known_text_question: KnownTextQuestionCreate
):
    db_known_text_question = KnownTextQuestionModel(
        question=known_text_question.question,
        is_optional=known_text_question.is_optional,
        is_multiple_choice=known_text_question.is_multiple_choice,
    )
    db.add(db_known_text_question)
    db.commit()
    db.refresh(db_known_text_question)
    return db_known_text_question


def create_known_text_questions(
    db: Session, known_text_questions: List[KnownTextQuestionCreate]
):
    db_known_text_questions = []
    for known_text_question in known_text_questions:
        db_known_text_question = KnownTextQuestionModel(
            question=known_text_question.question,
            is_optional=known_text_question.is_optional,
            is_multiple_choice=known_text_question.is_multiple_choice,
        )
        db.add(db_known_text_question)
        db_known_text_questions.append(db_known_text_question)
    db.commit()
    return db_known_text_questions


def update_known_text_question(
    db: Session, id: int, known_text_question: KnownTextQuestion
):
    db_known_text_question = (
        db.query(KnownTextQuestionModel).filter(KnownTextQuestionModel.id == id).first()
    )
    db_known_text_question.question = known_text_question.question
    db.commit()
    db.refresh(db_known_text_question)
    return db_known_text_question


def delete_known_text_question(db: Session, id: int):
    rows_deleted = (
        db.query(KnownTextQuestionModel)
        .filter(KnownTextQuestionModel.id == id)
        .delete()
    )
    db.commit()
    return rows_deleted
