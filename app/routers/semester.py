from app.logic import semester as logic
from app.db.schemas import semester as schema
from app.db.db import get_db

from sqlalchemy.orm import Session

from typing import List

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/semesters",
    tags=["semesters"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.Semester])
def get_semesters(db: Session = Depends(get_db)):
    semesters = logic.get_semesters(db)
    return semesters


@router.get("/{semester_id}", response_model=schema.Semester)
def get_semester_by_id(
    semester_id: int, db: Session = Depends(get_db)
):
    db_semester = logic.get_semester_by_id(db, semester_id)
    if db_semester is None:
        raise HTTPException(status_code=404, detail=f"Semester with id {semester_id} not found")
    return db_semester


@router.post("/", response_model=schema.Semester)
def create_semester(
    semester: schema.CreateSemester, db: Session = Depends(get_db)
):
    return logic.create_semester(db, semester)


@router.post("/bulk", response_model=List[schema.Semester])
def create_semesters(
    semesters: List[schema.CreateSemester], db: Session = Depends(get_db)
):
    return logic.create_semesters(db, semesters)


@router.put("/{semester_id}", response_model=schema.Semester)
def update_semester(
    semester_id: int, semester: schema.CreateSemester, db: Session = Depends(get_db)
):
    db_semester = logic.get_semester_by_id(db, semester_id)
    if db_semester is None:
        raise HTTPException(
            status_code=404, detail=f"Semester with id {id} not found"
        )
    return logic.update_semester(db, semester_id, semester)


@router.delete("/{semester_id}", response_model=schema.Semester)
def delete_semester(
    semester_id: int, db: Session = Depends(get_db)
):
    db_semester = logic.get_semester_by_id(db, semester_id)
    if db_semester is None:
        raise HTTPException(
            status_code=404, detail=f"Semester with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_semester(db, semester_id)} semester"
    }