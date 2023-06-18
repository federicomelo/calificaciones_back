from app.db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean

class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    section = Column(Integer, nullable=False)
    abbreviation = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    rounding_policy = Column(Integer, nullable=False)

    semester_id = Column(Integer, nullable=False)
    semester = relationship("Semester", back_populates="subjects")

    assignments = relationship("Assignment", back_populates="subject")