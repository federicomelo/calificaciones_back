from sqlalchemy.orm import Session
from app.db.base import Subject as SubjectModel
from app.db.schemas.subject import (
    Subject,
    CreateSubject,
)
from typing import List


def get_subject_by_id(db: Session, subject_id: int):
    return (
        db.query(SubjectModel)
        .filter(SubjectModel.id == subject_id)
        .first()
    )


def get_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SubjectModel).offset(skip).limit(limit).all()


def create_subject(
    db: Session, subject: CreateSubject
):
    db_subject = SubjectModel(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject


def create_subjects(
    db: Session, subjects: List[CreateSubject]
):
    db_subjects = [
        SubjectModel(**subject.dict()) for subject in subjects
    ]
    db.add_all(db_subjects)
    db.commit()
    return db_subjects


def update_subject(
    db: Session, subject_id: int, subject: Subject
):
    db_subject = (
        db.query(SubjectModel)
        .filter(SubjectModel.id == subject_id)
        .first()
    )
    db_subject.name = subject.name
    db_subject.code = subject.code
    db_subject.number = subject.number
    db_subject.section = subject.section
    db_subject.abbreviation = subject.abbreviation
    db_subject.credits = subject.credits
    db_subject.rounding_policy = subject.rounding_policy
    db_subject.semester_id = subject.semester_id
    db.commit()
    db.refresh(db_subject)
    return db_subject


def delete_subject(db: Session, subject_id: int):
    rows_deleted = (
        db.query(SubjectModel)
        .filter(SubjectModel.id == subject_id)
        .delete()
    )
    db.commit()
    return rows_deleted