import tkinter.messagebox
import customtkinter

from functools import partial
from tkinter import Menu, LEFT, BOTH
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from major import Major
from semester import Semester
from subject import Subject
from grade import Grade
from model import *
from typing import Iterable


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

MAJOR: Major = None

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Evaluación de desempeño académico")
        self.geometry(f"{1100}x{580}")

        # layout: two columns, four rows
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.create_sidebar()

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=1, rowspan=4, sticky="nsew", pady=0, padx=20)
        self.tabview.add("Carrera")
        self.tabview.add("Semestres")
        self.tabview.add("Cursos")

        self.tabview.tab("Carrera").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.main_graph(self.tabview.tab("Carrera"))

        self.tabview.tab("Semestres").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Semestres"), dynamic_resizing=False,
                                                        values=["2020-20", "2023-10"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))

    
    def main_graph(self, root: customtkinter.CTk) -> None:
        graph: Figure = MAJOR.performance_graph()
        canvas = FigureCanvasTkAgg(graph, root).get_tk_widget().pack(fill=BOTH, expand=True)


    def create_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Calificaciones", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.carrera = customtkinter.CTkButton(self.sidebar_frame, text="Carrera", command=self.sidebar_button_event)
        self.carrera.grid(row=1, column=0, padx=20, pady=10)

        self.semestres = customtkinter.CTkButton(self.sidebar_frame, text="Semestres",command=self.sidebar_button_event)
        self.semestres.grid(row=2, column=0, padx=20, pady=10)

        self.cursos = customtkinter.CTkButton(self.sidebar_frame, text="Cursos",command=self.sidebar_button_event)
        self.cursos.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Apariencia:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Zoom:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    MAJOR: Major = load_major()
    app = App()
    app.mainloop()