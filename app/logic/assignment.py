from sqlalchemy.orm import Session
from app.db.base import Assignment as AssignmentModel
from app.db.schemas.assignment import (
    Assignment,
    CreateAssignment,
)
from typing import List


def get_assignment_by_id(db: Session, assignment_id: int):
    return (
        db.query(AssignmentModel)
        .filter(AssignmentModel.id == assignment_id)
        .first()
    )


def get_assignments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AssignmentModel).offset(skip).limit(limit).all()


def get_assignments_by_subject_id(db: Session, subject_id: int):
    return (
        db.query(AssignmentModel)
        .filter(AssignmentModel.subject_id == subject_id)
        .all()
    )


def create_assignment(
    db: Session, assignment: CreateAssignment
):
    db_assignment = AssignmentModel(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment


def create_assignments(
    db: Session, assignments: List[CreateAssignment]
):
    db_assignments = [
        AssignmentModel(**assignment.dict()) for assignment in assignments
    ]
    db.add_all(db_assignments)
    db.commit()
    return db_assignments


def update_assignment(
    db: Session, assignment_id: int, assignment: Assignment
):
    db_assignment = (
        db.query(AssignmentModel)
        .filter(AssignmentModel.id == assignment_id)
        .first()
    )
    db_assignment.name = assignment.name
    db_assignment.percentage = assignment.percentage
    db_assignment.grade = assignment.grade
    db_assignment.comments = assignment.comments
    db_assignment.subject_id = assignment.subject_id
    db.commit()
    db.refresh(db_assignment)
    return db_assignment


def delete_assignment(db: Session, assignment_id: int):
    rows_deleted = (
        db.query(AssignmentModel)
        .filter(AssignmentModel.id == assignment_id)
        .delete()
    )
    db.commit()
    return rows_deleted