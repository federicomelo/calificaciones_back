from app.db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Float, Integer, String, ForeignKey

class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    section = Column(Integer, nullable=False)
    abbreviation = Column(String)
    credits = Column(Integer, nullable=False)
    rounding_policy = Column(Float, nullable=False, default=0.01)
    dropped = Column(Boolean, nullable=False, default=False)

    semester_id = Column(Integer, ForeignKey("semester.id"), nullable=False) 
    semester = relationship("Semester", back_populates="subjects")

    assignments = relationship("Assignment", back_populates="subject")