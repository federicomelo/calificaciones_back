from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.base import Survey as SurveyModel
from app.db.base import NumericQuestion as NumericQuestionModel
from app.db.base import TextQuestion as TextQuestionModel
from app.db.schemas.survey import (
    SurveySchema,
    SurveyCreateSchema,
    SurveyPaginatedSchema,
)
from app.db.schemas.numeric_question import (
    NumericQuestionCreate,
)
from app.db.schemas.text_question import TextQuestionCreate
from app.db.models.survey import SurveyKindEnum
from fastapi import UploadFile
from app.logic.user import get_user_by_name
from app.logic.known_numeric_question import get_known_numeric_questions
from app.logic.known_text_question import get_known_text_questions

from io import BytesIO
from pandas import read_excel


def get_survey(db: Session, id: int):
    return db.query(SurveyModel).filter(SurveyModel.id == id).first()


def get_survey_by_kind(db: Session, kind: str):
    return db.query(SurveyModel).filter(SurveyModel.kind == kind).first()


def get_paginated_surveys_by_tutor_login(
    db: Session, tutor_login: str, skip: int = 0, limit: int = 100
):
    return (
        db.query(SurveyModel)
        .filter(SurveyModel.tutor_login == tutor_login)
        .offset(skip)
        .limit(limit)
        .all(),
        db.query(SurveyModel).filter(SurveyModel.tutor_login == tutor_login).count(),
    )


def get_surveys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SurveyModel).offset(skip).limit(limit).all()


def create_survey(db: Session, survey: SurveyCreateSchema):
    db_survey = SurveyModel(
        kind=survey.kind,
        tutor_login=survey.tutor_login,
        numeric_questions=[],
        text_questions=[],
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey


def create_survey_from_excel(db: Session, survey: SurveyCreateSchema):
    db_survey = SurveyModel(
        kind=survey.kind,
        tutor_login=survey.tutor_login,
        numeric_questions=[],
        text_questions=[],
    )
    db.add(db_survey)
    db.flush()
    db.refresh(db_survey)
    return db_survey


def create_numeric_question_survey(
    db: Session, numeric_question: NumericQuestionCreate, survey_id: int
):
    if get_survey(db, survey_id) is None:
        return None
    question_dict = numeric_question.dict()
    if "survey_id" in question_dict:
        question_dict.pop("survey_id")
    db_numeric_question = NumericQuestionModel(**question_dict, survey_id=survey_id)
    db.add(db_numeric_question)
    db.commit()
    db.refresh(db_numeric_question)
    return db_numeric_question


def create_numeric_question_survey_excel(
    db: Session, numeric_question: NumericQuestionCreate
):
    db_numeric_question = NumericQuestionModel(**numeric_question.dict())
    db.add(db_numeric_question)
    return db_numeric_question


def create_text_question_survey(
    db: Session, text_question: TextQuestionCreate, survey_id: int
):
    if get_survey(db, survey_id) is None:
        return None
    question_dict = text_question.dict()
    if "survey_id" in question_dict:
        question_dict.pop("survey_id")

    db_text_question = TextQuestionModel(**question_dict, survey_id=survey_id)
    db.add(db_text_question)
    db.commit()
    db.refresh(db_text_question)
    return db_text_question


def create_text_question_survey_excel(
    db: Session,
    text_question: TextQuestionCreate,
):
    db_text_question = TextQuestionModel(**text_question.dict())
    db.add(db_text_question)
    return db_text_question


def create_surveys_from_excel(db: Session, file: UploadFile):
    df = read_excel(BytesIO(file.file.read()))

    drop_unnecesary_columns(df)

    kind = (
        SurveyKindEnum.normal.name
        if df.iloc[0]["Tipo de horario"] == "Normal"
        else SurveyKindEnum.express.name
    )

    return process_excel_data(db, df, kind)


def process_excel_data(db, df, kind):
    known_numeric_questions = get_known_numeric_questions(db)
    known_text_questions = get_known_text_questions(db)
    users_not_found = []

    try:
        for _, row in df.iterrows():
            user_name = row["Prestador del servicio"]
            user = get_user_by_name(db, user_name)
            if user is None:
                if user_name not in users_not_found:
                    users_not_found.append(user_name)
                continue

            login = user.login

            survey = create_survey_from_excel(
                db,
                SurveyCreateSchema(kind=kind, tutor_login=login),
            )

            for i in range(len(known_numeric_questions)):
                numeric_question = create_numeric_question_survey_excel(
                    db,
                    NumericQuestionCreate(
                        question=known_numeric_questions[i].question,
                        value=row[known_numeric_questions[i].question],
                        is_optional=known_numeric_questions[i].is_optional,
                        hidden=False,
                        survey_id=survey.id,
                    ),
                )
                survey.numeric_questions.append(numeric_question)

            for i in range(len(known_text_questions)):
                answer = row[known_text_questions[i].question]
                if type(answer) is not float:
                    text_question = create_text_question_survey_excel(
                        db,
                        TextQuestionCreate(
                            question=known_text_questions[i].question,
                            answer=answer,
                            is_optional=known_text_questions[i].is_optional,
                            is_multiple_choice=known_text_questions[
                                i
                            ].is_multiple_choice,
                            hidden=False,
                            survey_id=survey.id,
                        ),
                    )
                    survey.text_questions.append(text_question)

    except Exception as e:
        db.rollback()
        return False, f"An error occurred while processing the data: {str(e)}"
    if len(users_not_found) > 0:
        users_not_found_str = ", ".join(users_not_found)
        return False, f"Users {users_not_found_str} not found"

    db.commit()
    return True, len(df)


def drop_unnecesary_columns(df):
    df.drop(df[df["Estado"] == "Inválida"].index, inplace=True)

    always_empty_cols = ["Fecha de devolución"]
    # Might prove to be useful later... but not for the MVP
    uneccesary_cols = [
        "Fecha inicio",
        "Fecha fin",
        "Fecha de llegada",
        "Estado de la reserva",
        "Prioritaria",
    ]
    df.drop(columns=always_empty_cols + uneccesary_cols, inplace=True)


def update_survey(db: Session, id: int, survey: SurveySchema):
    db_survey = db.query(SurveyModel).filter(SurveyModel.id == id).first()
    db_survey.kind = survey.kind
    db.commit()
    db.refresh(db_survey)
    return db_survey


def delete_survey(db: Session, id: int):
    rows_deleted = db.query(SurveyModel).filter(SurveyModel.id == id).delete()
    db.commit()
    return rows_deleted
