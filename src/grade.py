from __future__ import annotations


class Bonus:

    points: float = .0
    reason: str = ""

    def __init__(self, *args) -> None:
        """
        May recieve one or more arguments, equivalent to:
        points, reason
        """
        match args:
            case (points, reason):
                self.points = points
                self.reason = reason
            case points:
                self.points = points

    def __repr__(self) -> None:
        return f"Bono de {self.points} ({self.reason})"

    def as_dict(self) -> dict:
        return {"points": self.points, "reason": self.reason}

    def from_dict(dict_: dict) -> Bonus:
        return Bonus(dict_["points"], dict_["reason"])


class Grade:

    name: str = ""
    grade: int = 0
    percentage: float = .0
    comments: str = ""
    bonus_points: Bonus = None

    def __init__(self, *args) -> None:
        """
        May recieve one or more arguments, equivalent to:
        name, percentage, grade, comments
        """
        match args:
            case (name, percentage, grade, comments):
                self.name = name
                self.percentage = percentage
                self.grade = grade
                self.comments = comments
            case (name, percentage, grade):
                self.name = name
                self.percentage = percentage
                self.grade = grade
            case (name, percentage):
                self.name = name
                self.percentage = percentage
            case name:
                self.name = name

    def __repr__(self) -> None:
        s: str = f"{self.name}. Porcentaje: {self.percentage}, Nota: {self.grade}."
        s += f" Comentarios: {self.comments}." if self.comments else ""
        s += f" Bono: {str(self.bonus_points)}." if self.bonus_points else ""
        return s

    def as_dict(self) -> dict:
        dict_ = {
            "name": self.name,
            "grade": self.grade,
            "percentage": self.percentage
        }
        comments: dict = {"comments": self.comments} if self.comments else {}
        dict_.update(comments)
        bonus: dict = {"bonus_points": self.bonus_points.as_dict()
                       } if self.bonus_points else {}
        dict_.update(bonus)
        return dict_

    def set_bonus(self, bonus: Bonus) -> None:
        self.bonus_points = bonus

    def from_dict(dict_: str) -> Grade:
        if "comments" in dict_:
            grade = Grade(dict_["name"], dict_["percentage"], dict_["grade"], dict_["comments"])
        else:
            grade = Grade(dict_["name"], dict_["percentage"], dict_["grade"])
        if "bonus_points" in dict_:
            grade.set_bonus(Bonus.from_dict(dict_["bonus_points"]))
        return grade
