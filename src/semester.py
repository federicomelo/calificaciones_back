from __future__ import annotations
from ordinal import Ordinal
from grade import Grade
from subject import Subject
from typing import Iterable


class Semester:

    name: str = ""
    number: int = 0
    year: int = 0
    period: int = 10
    subjects: list[Subject] = []

    def __init__(self, year: int, period: int) -> None:
        self.year: int = year
        self.period: int = period

        # 2020-20 -> 1, 2021-10 -> 2, 2021-20 -> 3, 2022-10 -> 4, etc.
        self.number: int = year*2 - 4041 + period // 10

        self.name: str = str(Ordinal(self.number, apocopado=True)
                             ).title() + " semestre"

    def add_subject(self, subject: Subject) -> None:
        self.subjects.append(subject)

    def add_subjects(self, subjects: Iterable[Subject]) -> None:
        self.subjects.extend(subjects)

    def as_dict(self) -> None:
        return {
            "name": self.name,
            "number": self.number,
            "year": self.year,
            "period": self.period,
            "subjects": [subject.as_dict() for subject in self.subjects]
        }

    def from_json(data: str) -> Semester:
        from json import loads
        dict_ = loads(data)
        sem = Semester(dict_["year"], dict_["period"])
        sem.subjects = [Subject.from_dict(subject)
                        for subject in dict_["subjects"]]
        return sem

    def __repr__(self) -> str:
        return f"{self.name} ({self.year}-{self.period})"
