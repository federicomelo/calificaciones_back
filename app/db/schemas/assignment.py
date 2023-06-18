from pydantic import BaseModel


class AssignmentBase(BaseModel):
    name: str
    percentage: float
    grade: float
    comments: str


class AssignmentCreate(AssignmentBase):
    subject_id: int


class Assignment(AssignmentBase):
    id: int
    subject_id: int

    class Config:
        orm_mode = True
