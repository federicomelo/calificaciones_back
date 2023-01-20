from json import dump
from semester import Semester
from subject import Subject
from grade import Grade
from pathlib import Path
from re import split

SRC: str = str(Path(__file__).parent.absolute())
DATA: str = str(Path(__file__).parent.parent.absolute()) + "/data"

def persist_semester(sem: Semester) -> None:
    print(sem.as_dict())
    json: str = "/"+str(sem.year)+"-"+str(sem.period)+".json"
    with open(DATA+json, "w+") as file:
        dump(sem.as_dict(), file, indent=4, ensure_ascii=False)
        file.close()


def import_semester(year: int, period: int) -> Semester:
    json: str = "/"+str(year)+"-"+str(period)+".json"
    with open(DATA+json, "r") as file:
        data = file.read()
        file.close()
        sem = Semester.from_json(data)
    return sem


def load_grades_from_tsv(path: str) -> None:
    semester_file = open(path, encoding="UTF-8")

    first_line = semester_file.readline()
    year_period = first_line.split()[2].strip()  # "2020-10"
    year = int(year_period[:4])
    period = int(year_period[5:])
    sem = Semester(year, period)

    file_as_list = split(r"\n\t*\n\t*\n", semester_file.read())
    sem.add_subjects(map(subjects_from_list, file_as_list))

    persist_semester(sem)


def subjects_from_list(subject_grades_str: str) -> Subject:
    lines = split("\n", subject_grades_str)

    title_line = lines[0].split()
    codigo = title_line[0]+" "+title_line[1][:-1]
    seccion = int(title_line[2][:-1])
    nombre = " ".join(title_line[3:-2])
    sub = Subject(nombre, 3, codigo, seccion)

    grades_list = lines[2:]

    grades = filter(lambda x: x is not None, map(read_grade, grades_list))
    # Con sub.add_grades mete todas las notas a todo mundo!!!!
    sub.set_grades(grades)

    return sub


def read_grade(grade_str: str) -> Grade | None:
    splitted = split("\t", grade_str)
    name = splitted[0]
    if "nota final".lower() in name.lower():
        return None
    else:
        try:
            gra = float(splitted[1])
            percentage = float(splitted[3][:-1])/100
            return Grade(name, percentage, gra)
        except Exception:
            return Grade(name, 0, 0, "".join(splitted[1:]))


if __name__ == "__main__":
    load_grades_from_tsv(DATA+"/2.tsv")
