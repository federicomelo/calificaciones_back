from sqlalchemy.orm import Session
from app.db.base import NumericQuestion as NumericQuestionModel
from app.db.schemas.numeric_question import NumericQuestion, NumericQuestionCreate


def get_numeric_question(db: Session, id: int):
    return db.query(NumericQuestionModel).filter(NumericQuestionModel.id == id).first()


def get_numeric_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NumericQuestionModel).offset(skip).limit(limit).all()


def create_numeric_question(db: Session, numeric_question: NumericQuestionCreate):
    db_numeric_question = NumericQuestionModel(
        question=numeric_question.question,
        is_optional=numeric_question.is_optional,
        value=numeric_question.value,
        hidden=numeric_question.hidden,
    )
    db.add(db_numeric_question)
    db.commit()
    db.refresh(db_numeric_question)
    return db_numeric_question


def update_numeric_question(db: Session, id: int, numeric_question: NumericQuestion):
    db_numeric_question = (
        db.query(NumericQuestionModel).filter(NumericQuestionModel.id == id).first()
    )
    db_numeric_question.question = numeric_question.question
    db_numeric_question.is_optional = numeric_question.is_optional
    db_numeric_question.value = numeric_question.value
    db_numeric_question.hidden = numeric_question.hidden
    db.commit()
    db.refresh(db_numeric_question)
    return db_numeric_question


def delete_numeric_question(db: Session, id: int):
    rows_deleted = (
        db.query(NumericQuestionModel).filter(NumericQuestionModel.id == id).delete()
    )
    db.commit()
    return rows_deleted
