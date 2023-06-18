from app.logic import survey as logic
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import survey as schemas
from app.db.schemas import numeric_question as numeric_question_schema
from app.db.schemas import text_question as text_question_schema
from starlette.responses import Response
from fastapi import File, UploadFile

router = APIRouter(
    prefix="/surveys",
    tags=["surveys"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[schemas.SurveySchema])
def get_surveys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    surveys = logic.get_surveys(db, skip=skip, limit=limit)
    return surveys


@router.get("/{id}", response_model=schemas.SurveySchema)
def get_survey(id: int, db: Session = Depends(get_db)):
    db_survey = logic.get_survey(db, id=id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail=f"Survey with id {id} not found")
    return db_survey


@router.post("/", response_model=schemas.SurveySchema)
def create_survey(
    surveySchema: schemas.SurveyCreateSchema, db: Session = Depends(get_db)
):
    return logic.create_survey(db=db, survey=surveySchema)


@router.post(
    "/{id}/numeric_questions/", response_model=numeric_question_schema.NumericQuestion
)
def create_numeric_question_for_survey(
    id: int,
    numeric_question: numeric_question_schema.NumericQuestionCreate,
    db: Session = Depends(get_db),
):
    answ_create = logic.create_numeric_question_survey(
        db=db, numeric_question=numeric_question, survey_id=id
    )
    if answ_create is None:
        raise HTTPException(status_code=404, detail=f"Survey with id {id} not found")
    return answ_create


@router.post("/{id}/text_questions/", response_model=text_question_schema.TextQuestion)
def create_text_question_for_survey(
    id: int,
    numeric_question: text_question_schema.TextQuestionCreate,
    db: Session = Depends(get_db),
):
    answ_create = logic.create_text_question_survey(
        db=db, text_question=numeric_question, survey_id=id
    )
    if answ_create is None:
        raise HTTPException(status_code=404, detail=f"Survey with id {id} not found")
    return answ_create


@router.post("/excel")
def create_survey_from_excel(
    db: Session = Depends(get_db),
    file: UploadFile = File(...),
):
    if (
        file.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(400, detail="Invalid document type")

    result = logic.create_surveys_from_excel(db=db, file=file)
    if not result[0]:
        raise HTTPException(400, detail=result[1])
    return {"detail": f"{result[1]} surveys created"}


@router.put("/{id}", response_model=schemas.SurveySchema)
def update_survey(
    id: int, surveySchema: schemas.SurveyCreateSchema, db: Session = Depends(get_db)
):
    db_survey = logic.get_survey(db, id=id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail=f"Survey with id {id} not found")
    return logic.update_survey(db=db, id=id, survey=surveySchema)


@router.delete("/{id}")
def delete_survey(id: int, db: Session = Depends(get_db)):
    db_survey = logic.get_survey(db, id=id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail=f"Survey with id {id} not found")
    return {"detail": f"Deleted {logic.delete_survey(db=db, id=id)} survey"}
