from typing import Optional
from pydantic import BaseModel


class AssignmentBase(BaseModel):
    name: str
    percentage: float
    grade: float
    comments: Optional[str] = None
    subject_id: int


class CreateAssignment(AssignmentBase):
    pass


class Assignment(AssignmentBase):
    id: int
    subject_id: int

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 101,  # This id is ignored by the database, which assigns its own id
                "name": "Exposición: Deloitte Value Map",
                "percentage": 0.05,
                "grade": 5.0,
                "comments": "La preparé con mi papi :)",
                "subject_id": 1  # TODO: id referencing Arquiemp
            }
        }
