from app.data.examples import ASSIGNMENTS
from app.logic import assignment as logic
from app.db.schemas import assignment as schema
from app.db.db import get_db

from sqlalchemy.orm import Session

from typing import Annotated, List

from fastapi import APIRouter, Body, Depends, HTTPException

router = APIRouter(
    prefix="/assignments",
    tags=["assignments"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schema.Assignment])
def get_assignments(db: Session = Depends(get_db)):
    assignments = logic.get_assignments(db)
    return assignments


@router.get("/{assignment_id}", response_model=schema.Assignment)
def get_assignment_by_id(
    assignment_id: int, db: Session = Depends(get_db)
):
    db_assignment = logic.get_assignment_by_id(db, assignment_id)
    if db_assignment is None:
        raise HTTPException(status_code=404, detail=f"Assignment with id {assignment_id} not found")
    return db_assignment


@router.post("/", response_model=schema.Assignment)
def create_assignment(
    assignment: schema.CreateAssignment, db: Session = Depends(get_db)
):
    return logic.create_assignment(db, assignment)


@router.post("/bulk", response_model=List[schema.Assignment])
def create_assignments(
    assignments: Annotated[
        List[schema.CreateAssignment],
        Body(example=ASSIGNMENTS)
    ], db: Session = Depends(get_db)
):
    return logic.create_assignments(db, assignments)


@router.put("/{assignment_id}", response_model=schema.Assignment)
def update_assignment(
    assignment_id: int, assignment: schema.CreateAssignment, db: Session = Depends(get_db)
):
    db_assignment = logic.get_assignment_by_id(db, assignment_id)
    if db_assignment is None:
        raise HTTPException(
            status_code=404, detail=f"Assignment with id {id} not found"
        )
    return logic.update_assignment(db, assignment_id, assignment)


@router.delete("/{assignment_id}", response_model=schema.Assignment)
def delete_assignment(
    assignment_id: int, db: Session = Depends(get_db)
):
    db_assignment = logic.get_assignment_by_id(db, assignment_id)
    if db_assignment is None:
        raise HTTPException(
            status_code=404, detail=f"Assignment with id {id} not found"
        )
    return {
        "detail": f"Deleted {logic.delete_assignment(db, assignment_id)} assignment"
    }


@router.get("/subject/{subject_id}", response_model=List[schema.Assignment])
def get_assignments_by_subject_id(
    subject_id: int, db: Session = Depends(get_db)
):
    assignments = logic.get_assignments_by_subject_id(db, subject_id)
    return assignments