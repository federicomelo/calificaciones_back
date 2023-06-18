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

        schema_extra = {
            "example": {
                "id": 101,  # This id is ignored by the database, which assigns its own id
                "year": 2023,
                "period": 10,
                # "student_id": 1
            }
        }