from semester import Semester
from subject import Subject
from matplotlib.pyplot import Figure
class Major:

    name = ""
    abbreviation = ""
    semesters = []

    def __init__(self, name: str, abbreviation: str, semesters: list[Semester]):
        self.name = name
        self.abbreviation = abbreviation
        self.semesters = semesters

    def __repr__(self):
        return f"Carrera: {self.name} ({self.abbreviation})"

    def gpa(self) -> float:
        return sum(semester.average() for semester in self.semesters) / len(self.semesters)

    def performance_graph(self) -> Figure:
        averages: list[float] = list(map(lambda sem: sem.average(), self.semesters))
        names: list[str] = list(map(lambda sem: sem.name, self.semesters))
        figure: Figure = Figure(figsize=(6,5), dpi=100)
        ax = figure.add_subplot(111)
        ax.plot(names, averages, color="green", marker="o")

        # background
        figure.patch.set_facecolor("#DBDBDB")
        ax.patch.set_facecolor("#DBDBDB")

        for a,b in zip(names, averages): 
            ax.text(a, round(b, 2)+0.05, str(round(b, 2)), ha='center', va='bottom', fontsize=10, color="black")
        
        return figure
