from app.db.db import Base
from sqlalchemy import Column, Integer, String, Boolean

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    section = Column(Integer, nullable=False)
    abbreviation = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    rounding_policy = Column(Integer, nullable=False)
    semester_id = Column(Integer, nullable=False)

    