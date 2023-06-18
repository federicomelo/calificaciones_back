from pydantic import BaseModel


class BaseSubject(BaseModel):
    # name, code, number, section, abbreviation, credits, rounding_policy
    name: str
    code: str
    number: int
    section: int
    abbreviation: str
    credits: float
    rounding_policy: float


class CreateSubject(BaseSubject):
    semester_id: int


class Subject(BaseSubject):
    id: int
    semester_id: int

    class Config:
        orm_mode = True
        