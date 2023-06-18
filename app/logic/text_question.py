from sqlalchemy.orm import Session
from app.db.base import TextQuestion as TextQuestionModel
from app.db.schemas.text_question import TextQuestion, TextQuestionCreate


def get_text_question(db: Session, id: int):
    return db.query(TextQuestionModel).filter(TextQuestionModel.id == id).first()


def get_text_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TextQuestionModel).offset(skip).limit(limit).all()


def create_text_question(db: Session, text_question: TextQuestionCreate):
    db_text_question = TextQuestionModel(
        question=text_question.question,
        is_optional=text_question.is_optional,
        answer=text_question.answer,
        is_multiple_choice=text_question.is_multiple_choice,
        hidden=text_question.hidden,
    )
    db.add(db_text_question)
    db.commit()
    db.refresh(db_text_question)
    return db_text_question


def update_text_question(db: Session, id: int, text_question: TextQuestion):
    db_text_question = (
        db.query(TextQuestionModel).filter(TextQuestionModel.id == id).first()
    )
    db_text_question.question = text_question.question
    db_text_question.is_optional = text_question.is_optional
    db_text_question.answer = text_question.answer
    db_text_question.is_multiple_choice = text_question.is_multiple_choice
    db_text_question.hidden = text_question.hidden
    db.commit()
    db.refresh(db_text_question)
    return db_text_question


def delete_text_question(db: Session, id: int):
    rows_deleted = (
        db.query(TextQuestionModel).filter(TextQuestionModel.id == id).delete()
    )
    db.commit()
    return rows_deleted
