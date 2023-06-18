from app.db.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Assignment(Base):
    __tablename__ = "assignment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    percentage = Column(Integer, nullable=False)
    grade = Column(Integer, nullable=False)
    comments = Column(String, nullable=False)

    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)
    subject = relationship("Subject", back_populates="assignments")

