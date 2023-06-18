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

        schema_extra = {
            "example": {
                "id": 101,  # This id is ignored by the database, which assigns its own id
                "name": "Arquitectura Empresarial",
                "code": "ISIS",
                "number": "2403",
                "section": 2,
                "abbreviation": "Arquiemp",
                "credits": 3,
                "rounding_policy": 0.5,
                "semester_id": 7
            }
        }
