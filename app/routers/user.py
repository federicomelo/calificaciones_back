from app.logic import user
from typing import List
from fastapi import APIRouter, Depends, HTTPException, File
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.db.schemas import user as user_schemas
from app.db.schemas import survey as survey_schemas
from app.logic.survey import get_paginated_surveys_by_tutor_login
from fastapi import File, UploadFile


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"detail": "Not found"}},
)


@router.get("/", response_model=List[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{login}", response_model=user_schemas.User)
def read_user(login: str, db: Session = Depends(get_db)):
    db_user = user.get_user(db, login=login)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return db_user


@router.get("/{login}/surveys", response_model=survey_schemas.SurveyPaginatedSchema)
def read_user_surveys(
    login: str, db: Session = Depends(get_db), page: int = 1, limit: int = 10
):
    db_user = user.get_user(db, login=login)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    result = get_paginated_surveys_by_tutor_login(
        db=db, tutor_login=login, skip=limit * (page - 1), limit=limit
    )
    return {
        "items": result[0],
        "count": result[1],
    }


@router.post("/", response_model=user_schemas.User)
def create_user(userSchema: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user.get_user(db, login=userSchema.login)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail=f"User with login {userSchema.login} already registered",
        )
    return user.create_user(db=db, user=userSchema)


@router.post("/csv")
def create_users_from_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if file.content_type != "text/csv":
        raise HTTPException(400, detail="Invalid document type")

    result = user.create_users_from_csv(db=db, file=file)
    if not result[0]:
        raise HTTPException(400, detail=result[1])
    return {"detail": f"{result[1]} new users created"}


@router.put("/{login}", response_model=user_schemas.User)
def update_user(
    login: str, userSchema: user_schemas.UserCreate, db: Session = Depends(get_db)
):
    db_user = user.get_user(db, login=login)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return user.update_user(db=db, login=login, user=userSchema)


@router.delete("/{login}")
def delete_user(login: str, db: Session = Depends(get_db)):
    db_user = user.get_user(db, login=login)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with login {login} not found"
        )
    return {"detail": f"Deleted {user.delete_user(db=db, login=login)} user"}
