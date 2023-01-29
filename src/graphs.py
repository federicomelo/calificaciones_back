


def subjects_bar_graph(subjects: list[Subject], root) -> None:
    """Generates a bar graph with the subjects and their respective grades"""
    subjects_names = [subject.name for subject in subjects]
    subjects_grades = [subject.grade for subject in subjects]

    figure = plt.Figure(figsize=(6,5), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot(subjects_names, subjects_grades, color="green", marker="o")
    ax.set_title("Gráfica de barras de las materias y sus notas")
    ax.set_xlabel("Materias")
    ax.set_ylabel("Notas")

    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()

