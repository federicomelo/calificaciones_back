from app.logic import subject as logic
from app.db.schemas import subject as schema
from app.db.db import get_db

from sqlalchemy.orm import Session

from typing import List

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/subjects",
    tags=["subjects"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.Subject])
def get_subjects(db: Session = Depends(get_db)):
    subjects = logic.get_subjects(db)
    return subjects


@router.get("/{subject_id}", response_model=schema.Subject)
def get_subject_by_id(
    subject_id: int, db: Session = Depends(get_db)
):
    db_subject = logic.get_subject_by_id(db, subject_id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail=f"Subject with id {subject_id} not found")
    return db_subject


@router.post("/", response_model=schema.Subject)
def create_subject(
    subject: schema.CreateSubject, db: Session = Depends(get_db)
):
    return logic.create_subject(db, subject)


@router.post("/bulk", response_model=List[schema.Subject])
def create_subjects(
    subjects: List[schema.CreateSubject], db: Session = Depends(get_db)
):
    return logic.create_subjects(db, subjects)


@router.put("/{subject_id}", response_model=schema.Subject)
def update_subject(
    subject_id: int, subject: schema.CreateSubject, db: Session = Depends(get_db)
):
    db_subject = logic.get_subject_by_id(db, subject_id)
    if db_subject is None:
        raise HTTPException(
            status_code=404, detail=f"Subject with id {id} not found"
        )
    return logic.update_subject(db, subject_id, subject)


@router.delete("/{subject_id}", response_model=schema.Subject)
def delete_subject(
    subject_id: int, db: Session = Depends(get_db)
):
    db_subject = logic.get_subject_by_id(db, subject_id)
    if db_subject is None:
        raise HTTPException(
            status_code=404, detail=f"Subject with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_subject(db, subject_id)} subject"
    }