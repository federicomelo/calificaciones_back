from app.db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean


class Semester(Base):
    __tablename__ = "semester"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    period = Column(Integer, nullable=False)

    subjects = relationship("Subject", back_populates="semester")