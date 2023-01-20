from semester import Semester
from subject import Subject
from grade import Grade
from model import persist_semester, import_semester

def menu() -> None:
    while True:
        try:
            print("Menú principal\n")
            print("1. Nuevo semestre\n")
            print("2. Seleccionar semestre\n")
            selection: str = input("Seleccione una opción: ")
            if selection == "1":
                get_semester(1)
            elif selection == "2":
                get_semester(2)
        except KeyboardInterrupt:
            print("\nSaliendo...")
            exit()


def get_semester(new_or_select: int) -> None:
    try: 
        year = int(input("Año del semestre\nE.g: 2021\n> "))
    except ValueError:
        print("El año debe ser un número entero")
        semester(new_or_select)
    try:
        period = int(input("Periodo del semestre\n10 para primer semestre del año, 20 para segundo\n> "))
    except ValueError:
        print("El periodo debe ser un número entero")
        semester(new_or_select)
    if new_or_select == 1:
        semester = Semester(year, period)
    elif new_or_select == 2:
        semester = import_semester(year, period)
    semester_menu(semester)


def semester_menu(semester: Semester) -> None:
    print(f"Menú de {semester.name}\n")
    print("1. Agregar materia\n")
    print("2. Persistir semestre\n")
    selection = input("Seleccione una opción: ")
    if selection == "1":
        new_subject(semester)
    elif selection == "2":
        persist_semester(semester)


def new_subject(semester: Semester) -> None:
    name = input(
        "Nombre de la materia\nE.g: Diseño y Análisis de Algoritmos\n> ")
    code = input("Código de la materia\nE.g: ISIS 1105\n> ")
    code = code.replace("-", " ")
    credits = int(input("Créditos de la materia\nE.g: 3\n> "))
    section = int(input("Sección de la materia\nE.g: 1\n> "))
    nickname = input("Apodo de la materia\nE.g: Dalgo\n> ")
    subject = Subject(name, credits, code, section, nickname)
    semester.add_subject(subject)
    subject_menu(subject, semester)


def subject_menu(subject: Subject, semester: Semester) -> None:
    print(f"Menú de {subject.nickname} ({semester.name})\n")
    print("1. Agregar nota\n")
    print("2. Volver a menú de semestre\n")
    selection = input("Seleccione una opción: ")
    if selection == "1":
        new_grade(subject, semester)
    elif selection == "2":
        semester_menu(semester)


def new_grade(subject: Subject, semester: Semester) -> None:
    name = input("Nombre de la nota\nE.g: Parcial 2: Programación dinámica y algoritmos sobre grafos\n> ")
    try:
        grade = float(input("Nota sobre 5\nE.g: 5.0\n> "))
    except ValueError:
        print("La nota debe ser un número decimal entre 0.0 y 5.0")
        new_grade(subject, semester)
    percentage = float(input("Porcentaje de la nota\nE.g: 0.2\n> "))
    comments = input("Observaciones\nSi no hay ninguna, solo presione Enter\n> ")
    grade = Grade(name, grade, percentage, comments)
    subject.add_grade(grade)
    subject_menu(subject, semester)


if __name__ == "__main__":
    menu()