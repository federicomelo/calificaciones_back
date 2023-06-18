from sqlalchemy.orm import Session
from app.db.models.user import User as UserModel
from app.db.schemas.user import User as UserSchema
from fastapi import UploadFile
from io import BytesIO
import pandas as pd


def get_user(db: Session, login: str):
    return db.query(UserModel).filter(UserModel.login == login).first()


def get_user_by_name(db: Session, name: str):
    return db.query(UserModel).filter(UserModel.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def get_users_by_role(db: Session, role: str):
    return db.query(UserModel).filter(UserModel.role == role).all()


def create_user(db: Session, user: UserSchema):
    db_user = UserModel(
        name=user.name, nickname=user.nickname, role=user.role, login=user.login
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_from_csv(db: Session, user: UserSchema):
    db_user = UserModel(
        name=user.name, nickname=user.nickname, role=user.role, login=user.login
    )
    db.add(db_user)
    db.flush()
    db.refresh(db_user)
    return db_user


def create_users_from_csv(db: Session, file: UploadFile):
    df = pd.read_csv(BytesIO(file.file.read()))
    new_user_count = 0
    try:
        for _, row in df.iterrows():
            if get_user(db, row["login"]) is None:
                user = UserSchema(
                    name=row["nombre"].strip(),
                    nickname=row["nombre"].strip(),
                    role="tutor",
                    login=row["login"].strip(),
                )
                create_user_from_csv(db, user)
                new_user_count += 1
    except Exception as e:
        db.rollback()
        return False, f"Error while creating users: {str(e)}"
    db.commit()
    return True, new_user_count


def update_user(db: Session, login: str, user: UserSchema):
    db_user = db.query(UserModel).filter(UserModel.login == login).first()
    db_user.name = user.name
    db_user.nickname = user.nickname
    db_user.role = user.role
    db_user.login = user.login
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, login: str):
    rows_deleted = db.query(UserModel).filter(UserModel.login == login).delete()
    db.commit()
    return rows_deleted
