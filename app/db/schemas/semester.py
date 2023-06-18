from pydantic import BaseModel


class BaseSemester(BaseModel):
    year: int
    period: int


class CreateSemester(BaseSemester):
    # student_id: int
    pass


class Semester(BaseSemester):
    id: int
    # student_id: int

    class Config:
        orm_mode = True