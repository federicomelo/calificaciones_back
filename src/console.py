from functools import partial
from tkinter import Menu, LEFT, BOTH
from customtkinter import CTk, CTkLabel, CTkOptionMenu, CTkFrame, CTkButton, CTkTabview, CTkFont
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from major import Major
from semester import Semester
from subject import Subject
from grade import Grade
from model import *
from typing import Iterable


def create_window(major: Major):
    app = CTk()
    app.geometry("400x240")

    app.title("Evaluación de desempeño académico")

    create_side_menu(app)

    create_tabs(app)
    

    app.mainloop()
    create_menu(app)
    main_graph(major, app)
    app.mainloop()






def add_menu_options(menubar: Menu) -> None:
    semester_menu, subject_menu, grade_menu = Menu(menubar, tearoff=0), Menu(
        menubar, tearoff=0), Menu(menubar, tearoff=0)

    add_semester_menu_options(semester_menu)
    add_subject_menu_options(subject_menu)

    menubar.add_cascade(label="Semestre", menu=semester_menu)
    menubar.add_cascade(label="Materia", menu=subject_menu)
    menubar.add_cascade(label="Nota", menu=grade_menu)


def add_semester_menu_options(semester_menu: Menu):
    select_semester_menu = Menu(semester_menu, tearoff=0)

    select_semester_menu.add_command(
        label="2020-20", command=partial(select_semester, 2020, 20))
    select_semester_menu.add_command(
        label="2021-10", command=partial(select_semester, 2021, 10))
    select_semester_menu.add_command(
        label="2021-20", command=partial(select_semester, 2021, 20))
    select_semester_menu.add_command(
        label="2022-10", command=partial(select_semester, 2022, 10))
    select_semester_menu.add_command(
        label="2022-19", command=partial(select_semester, 2022, 19))
    select_semester_menu.add_command(
        label="2022-20", command=partial(select_semester, 2022, 20))
    select_semester_menu.add_command(
        label="2023-10", command=partial(select_semester, 2023, 10))

    semester_menu.add_command(label="Nuevo semestre", command=new_semester)
    semester_menu.add_cascade(
        label="Seleccionar semestre", menu=select_semester_menu)


def add_subject_menu_options(subject_menu: Menu) -> None:
    subject_menu.add_command(label="Agregar materia",
                             command=new_subject)
    subject_menu.add_command(label="Seleccionar materia", command=show_subjects)
    subject_menu.add_command(label="Persistir semestre", command=persist_semester)


def new_semester() -> None:
    try:
        year = int(input("Año del semestre\nE.g: 2021\n> "))
    except ValueError:
        print("El año debe ser un número entero")
        new_semester()
    try:
        period = int(input(
            "Periodo del semestre\n10 para primer semestre del año, 20 para segundo\n> "))
    except ValueError:
        print("El periodo debe ser un número entero")
        new_semester()
    semester = Semester(year, period)


def select_semester(year: int, period: int) -> None:
    global SEMESTER
    SEMESTER = import_semester(year, period)
    


def show_subjects() -> None:
    subjects: list[Subject] = sorted(SEMESTER.subjects)
    i = 0
    while i < len(subjects):
        print(str(i+1) + ". " + str(subjects[i]) + "\n")
        i += 1
    print(str(i+1) + ". Volver al menú de semestre\n")
    try:
        selection = int(input("Seleccione una opción: "))
    except ValueError:
        print("La selección debe ser un número entero entre 1 y " + str(i+1))
    if selection == i+1:
        semester_menu(SEMESTER)
    else:
        subject: Subject = subjects[selection-1]
        subject_menu(subject, SEMESTER)


def new_subject() -> None:
    name = input(
        "Nombre de la materia\nE.g: Diseño y Análisis de Algoritmos\n> ")
    code = input("Código de la materia\nE.g: ISIS 1105\n> ")
    code = code.replace("-", " ")
    credits = int(input("Créditos de la materia\nE.g: 3\n> "))
    section = int(input("Sección de la materia\nE.g: 1\n> "))
    nickname = input("Apodo de la materia\nE.g: Dalgo\n> ")
    subject = Subject(name, credits, code, section, nickname)
    SEMESTER.add_subject(subject)
    subject_menu(subject, SEMESTER)


def subject_menu(subject: Subject, semester: Semester) -> None:
    print(f"Menú de {subject.nickname} ({semester.name})\n")
    print("1. Agregar nota\n")
    print("2. Ver o editar notas\n")
    print("3. Volver a menú de semestre\n")
    selection = input("Seleccione una opción: \n\n")
    if selection == "1":
        new_grade(subject, semester)
    elif selection == "2":
        show_grades(subject, semester)
    elif selection == "4":
        semester_menu(semester)


def show_grades(subject: Subject, semester: Semester) -> None:
    grades: list[Grade] = subject.grades
    i = 0
    while i < len(grades):
        print(str(i+1) + ". " + str(grades[i]) + "\n")
        i += 1
    print(str(i+1) + ". Volver al menú de materia\n")
    try:
        selection = int(input("Seleccione una opción: "))
    except ValueError:
        print("La selección debe ser un número entero entre 1 y " + str(i+1))
    if selection == i+1:
        subject_menu(subject, semester)
    else:
        grade: Grade = grades[selection-1]
        grade_menu(grade, subject, semester)


def grade_menu(grade: Grade, subject: Subject, semester: Semester) -> None:
    print(f"Menú de {grade.name} ({subject.nickname})\n")
    print("1. Editar nota\n")
    print("2. Editar porcentaje\n")
    print("3. Editar observaciones\n")
    print("4. Volver al menú de materia\n")
    selection = input("Seleccione una opción: \n\n")
    if selection == "1":
        edit_name(grade, subject, semester)
    elif selection == "2":
        edit_grade(grade, subject, semester)
    elif selection == "3":
        edit_percentage(grade, subject, semester)
    elif selection == "4":
        edit_comments(grade, subject, semester)
    elif selection == "5":
        subject_menu(subject, semester)


def edit_name(grade: Grade, subject: Subject, semester: Semester) -> None:
    grade.name = input("Nombre de la nota\nE.g: Examen 1\n> ")
    persist_semester(semester)
    grade_menu(grade, subject, semester)


def edit_grade(grade: Grade, subject: Subject, semester: Semester) -> None:
    try:
        grade.grade = float(input("Nota sobre 5\nE.g: 5.0\n> "))
    except ValueError:
        print("La nota debe ser un número decimal entre 0.0 y 5.0")
        edit_grade(grade, subject, semester)
    persist_semester(semester)
    grade_menu(grade, subject, semester)


def edit_percentage(grade: Grade, subject: Subject, semester: Semester) -> None:
    try:
        grade.percentage = float(input("Porcentaje de la nota\nE.g: 0.2\n> "))
    except ValueError:
        print("El porcentaje debe ser un número decimal entre 0.0 y 1.0")
        edit_percentage(grade, subject, semester)
    persist_semester(semester)
    grade_menu(grade, subject, semester)


def edit_comments(grade: Grade, subject: Subject, semester: Semester) -> None:
    grade.comments = input(
        "Observaciones\nSi no hay ninguna, solo presione Enter\n> ")
    persist_semester(semester)
    grade_menu(grade, subject, semester)


def new_grade(subject: Subject, semester: Semester) -> None:
    name = input(
        "Nombre de la nota\nE.g: Parcial 2: Programación dinámica y algoritmos sobre grafos\n> ")
    try:
        grade = float(input("Nota sobre 5\nE.g: 5.0\n> "))
    except ValueError:
        print("La nota debe ser un número decimal entre 0.0 y 5.0")
        new_grade(subject, semester)
    percentage = float(input("Porcentaje de la nota\nE.g: 0.2\n> "))
    comments = input(
        "Observaciones\nSi no hay ninguna, solo presione Enter\n> ")
    grade = Grade(name, percentage, grade, comments)
    subject.add_grade(grade)
    persist_semester(semester)
    subject_menu(subject, semester)


if __name__ == "__main__":
    major: Major = load_major()
    create_window(major)
