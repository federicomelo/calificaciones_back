from app.db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey


class Assignment(Base):
    __tablename__ = "assignment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    percentage = Column(Float)
    grade = Column(Float)
    comments = Column(String)

    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)
    subject = relationship("Subject", back_populates="assignments")

