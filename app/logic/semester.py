from sqlalchemy.orm import Session
from app.db.base import Semester as SemesterModel
from app.db.schemas.semester import (
    Semester,
    CreateSemester,
)
from typing import List


def get_semester_by_id(db: Session, semester_id: int):
    return (
        db.query(SemesterModel)
        .filter(SemesterModel.id == semester_id)
        .first()
    )


def get_semesters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SemesterModel).offset(skip).limit(limit).all()


def create_semester(
    db: Session, semester: CreateSemester
):
    db_semester = SemesterModel(**semester.dict())
    db.add(db_semester)
    db.commit()
    db.refresh(db_semester)
    return db_semester


def create_semesters(
    db: Session, semesters: List[CreateSemester]
):
    db_semesters = [
        SemesterModel(**semester.dict()) for semester in semesters
    ]
    db.add_all(db_semesters)
    db.commit()
    return db_semesters


def update_semester(
    db: Session, semester_id: int, semester: Semester
):
    db_semester = (
        db.query(SemesterModel)
        .filter(SemesterModel.id == semester_id)
        .first()
    )
    db_semester.year = semester.year
    db_semester.period = semester.period
    db.commit()
    db.refresh(db_semester)
    return db_semester


def delete_semester(db: Session, semester_id: int):
    rows_deleted = (
        db.query(SemesterModel)
        .filter(SemesterModel.id == semester_id)
        .delete()
    )
    db.commit()
    return rows_deleted