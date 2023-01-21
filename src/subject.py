from __future__ import annotations
from grade import Grade, Bonus
from typing import Iterable
from decimal import Decimal, ROUND_HALF_UP


class Subject:

    fullname: str = ""
    name: str = ""
    code: str = ""
    section: int = 0
    nickname: str = ""
    calculated_grade: float = .0
    final_grade: float = .0
    numeric_grade: bool = True
    credits: int = 0
    rounding_policy: float = .01
    grades: list[Grade] = []
    discussion: Subject = None
    laboratory: Subject = None
    bonus_points: Bonus = None

    def __init__(self, *args) -> None:
        """
        May recieve one or more arguments, equivalent to:
        name, credits, code, section, nickname
        """
        match args:
            case (name, credits, code, section, nickname):
                self.name = name
                self.credits = credits
                self.code = code
                self.section = section
                self.nickname = nickname
                self.fullname = self.code + ", " + \
                    str(self.section) + ": " + self.name + \
                    " (" + self.nickname + ")"
            case (name, credits, code, section):
                self.name = name
                self.credits = credits
                self.code = code
                self.section = section
                self.fullname = self.code + ", " + \
                    str(self.section) + ": " + self.name
            case (name, credits, code):
                self.name = name
                self.credits = credits
                self.code = code
                self.fullname = self.code + ": " + self.name
            case (name, credits):
                self.name = name
                self.credits = credits
                self.fullname = self.name

    def calculate_final_grade(self) -> None:
        bonus: float = self.bonus_points.points if self.bonus_points else .0
        self.final_grade = min(5.0, self.round_grade(
            self.calculated_grade + bonus))

    def round_grade(self, grade: float) -> float:
        """
        Rounds the calculated grade to obtain final grade based on rounding policy
        Rounding policy may be:
        1  : 4.743 rounds to 5
        .5 : 4.743 rounds to 4.5
        .25: 4.743 rounds to 4.75
        .1 : 4.743 rounds to 4.7
        .01: 4.743 rounds to 4.74 (default)
        """
        factor: float = 1/self.rounding_policy
        return float(Decimal(grade * factor).quantize(0, ROUND_HALF_UP)) / factor

    def add_grade(self, grade: Grade):
        if not self.numeric_grade:
            raise Exception("Subject doesn't have numeric grade")
        self.grades.append(grade)
        self.calculate_grade()
        self.calculate_final_grade()

    def add_grades(self, grades: Iterable[Grade]):
        if not self.numeric_grade:
            raise Exception("Subject doesn't have numeric grade")
        self.grades.extend(grades)
        self.calculate_grade()
        self.calculate_final_grade()

    def set_grades(self, grades: Iterable[Grade]):
        if not self.numeric_grade:
            raise Exception("Subject doesn't have numeric grade")
        self.grades = []
        self.grades.extend(grades)
        self.calculate_grade()
        self.calculate_final_grade()

    def calculate_grade(self) -> None:
        if self.grades:
            num: float = sum(
                map(lambda x: x.grade * x.percentage, self.grades))
            den: float = sum(map(lambda x: x.percentage, self.grades))
            if den != 0:
                self.calculated_grade = num / den

    def as_dict(self) -> None:
        dict_ = {
            "fullname": self.fullname,
            "name": self.name,
            "code": self.code,
            "section": self.section,
        }
        dict_.update({"nickname": self.nickname} if self.nickname else {})
        dict_.update({
            "credits": self.credits,
            "numeric": self.numeric_grade,
            "grades": [grade.as_dict() for grade in self.grades]
        })
        dict_.update({"discussion": self.discussion.as_dict()}
                     if self.discussion else {})
        dict_.update({"laboratory": self.laboratory.as_dict()}
                     if self.laboratory else {})
        dict_.update({
            "calculated_grade": self.calculated_grade
        })
        dict_.update({"bonus_points": self.bonus_points.as_dict()}
                     if self.bonus_points else {})
        dict_.update({
            "rounding_policy": self.rounding_policy,
            "final_grade": self.final_grade,
        })
        return dict_

    def set_bonus_points(self, bonus: Bonus):
        self.bonus_points = bonus
        self.calculate_final_grade()

    def from_dict(dict_: str) -> Subject:
        if "nickname" in dict_:
            subject = Subject(
                dict_["name"], dict_["credits"], dict_["code"], dict_["section"], dict_["nickname"])
        else:
            subject = Subject(dict_["name"], dict_["credits"],
                              dict_["code"], dict_["section"])

        subject.numeric_grade = dict_["numeric"]
        subject.rounding_policy = dict_["rounding_policy"]

        subject.grades = [Grade.from_dict(grade) for grade in dict_["grades"]]
        if "discussion" in dict_:
            subject.discussion = Subject.from_dict(dict_["discussion"])
        if "laboratory" in dict_:
            subject.laboratory = Subject.from_dict(dict_["laboratory"])
        if "bonus_points" in dict_:
            subject.bonus_points = Bonus.from_dict(dict_["bonus_points"])

        subject.calculate_grade()
        subject.calculate_final_grade()
        return subject

    def __repr__(self) -> str:
        return self.fullname
