import json

m1 = """Podcast: Relación entre la Constitución de 1991 y la noción de DDHH	4,50	5,000000%
Párrafo: Ejemplo de colaboración armónica	4,40	5,000000%
Infografía: Rama judicial Colombia	5,00	10,000000%
Podcast: Acceso sin barreras a la interrupción voluntaria del embarazo	4,70	10,000000%
Quiz 1 módulo de economía	4,50	5,250000%
Quiz 2 módulo de economía	5,00	5,250000%
Texto argumentativo módulo de economía	4,00	4,500000%
Texto: Igualdad y no discriminación	5,00	10,000000%
Texto: Recomendaciones de la OMS para el manejo de futuras pandemias	4,90	15,000000%
Infografía: Jurisdicción Especial para la Paz (JEP) y justicia transicional	4,80	15,000000%
Coevaluación	5,00	15,000000%"""

m2 = """Taller 1: Límites	4,60	10,00%
Examen parcial 1: Límites	5,00	20,00%
Examen parcial 2: Derivadas	5,00	20,00%
Taller 2: Optimización	4,90	10,00%
Examen parcial 3: Antiderivadas e integral definida	5,00	20,00%
Examen final	4,00	20,00%"""


m3 = """Quiz deductivo o inductivo	5,00	5,00%
Diagrama de lectura de Guy Debord 2.0: hacia un análisis de la mercantilización de la subjetividad en las redes sociales	4,58	10,00%
Planteamiento de tesis para el texto argumentativo	4,00	10,00%
Autoevaluación debate presidencial	5,00	5,00%
Quiz dialéctico y falacias	5,00	5,00%
Diagrama de texto argumentativo	4,48	10,00%
Texto argumentativo final	5,00	30,00%
Evaluación profesor debate Orator	5,00	5,00%
Coevaluación debate boxing	5,00	5,00%
Texto reflexivo	5,00	15,00%"""


m4 = """Párrafo sobre la importancia de la escritura	4,40	10,00%
Resumen de ¡Vamos al Centro Comercial! Consumo y visualidades del miedo en la Medellín contemporánea	4,65	25,00%
Reseña de Supermercados made in: Conexiones, consumo y apropiaciones. Estados Unidos y Colombia (siglo XX)	4,95	30,00%
Ejercicio de tildes	4,88	7,50%
Quiz de citación	5,00	7,50000%
Texto reflexivo	5,00	20,00%"""


m5 = """TODO"""


m6 = """Tareas nivel 1	5,00	1,00%
Proyecto nivel 1	4,60	4,00%
Examen nivel 1	4,65	5,00%
Tareas nivel 2	5,00	3,00%
Proyecto nivel 2	5,00	5,00%
Examen nivel 2	5,00	17,00%
Tareas nivel 3	5,00	4,00%
Examen nivel 3	5,00	25,00%
Proyecto nivel 3	5,00	6,00%
Tareas nivel 4	5,00	2,00%
Proyecto nivel 4	4,925	5,00%
Examen final	5,00	23,00%"""


m7 = """ Tarea 1: Péndulo simple	4,97	15,00%
Examen parcial 1	5,00	25,00%
Tarea 2: Osciladores acoplados	5,00	15,00%
Examen parcial 2: Expermiento osciladores acoplados	5,00	25,00%
Tarea 3: El descubrimiento de la violación de paridad	5,00	15,00%
Bono general del 5%	5,00	5,00%"""


m8 = """TODO"""


m9 = """Cumplimiento de la entrega no calificable 1: Acuerdos grupales	5,00	2,50000000000%
Cumplimiento de la entrega no calificable 2: Percepciones - Padlet 1	5,00	2,50000000000%
Cumplimiento de la entrega no calificable 3: Comparar Percepciones - Padlet 2	5,00	2,50000000000%
Tabla de análisis y contextualización de fuentes unidad 2	4,43	10,00000000000%
Plan de trabajo - historia de vida	4,50	2,50000000000%
Narrativa sobre la historia de vida familiar	5,00	25,00000000000%
Cumplimiento de la entrega no calificable 5: Justificación elección eje	5,00	3,33333333333%
Tabla de análisis y contextualización de fuentes unidad 3	5,00	10,00000000000%
Plan de trabajo grupal	4,00	5,00000000000%
Cumplimiento de la entrega no calificable 6: Foro: Contraste entre las fuentes	5,00	3,33333333333%
Cumplimiento de la entrega no calificable 7: Pregunta y justificación fuentes	5,00	3,33333333333%
Trabajo de indagación grupal	4,30	30,00000000000%"""


m10 = """TODO"""


m11 = """Complementaria FISI 1518, 16: Física 1	4,87	20,00%
FISI 1019, 22: Física Experimental I	5,00	20,00%
Quiz: Capítulo 1, secciones 1.1. a 3.3	4,70	4,00%
Examen parcial 1: Capítulos 1 a 5	5,00	12,00%
Examen parcial 2: Capítulos 6 a 9	5,06	12,00%
Examen parcial 3: Capítulos 10 a 14	3,93	12,00%
Examen final	4,50	20,00%"""


m12 = """Complementaria MATE 1214, 35: Cálculo Integral con Ecuaciones Diferenciales	5,00	15,00%
Examen parcial 1: Integración	4,60	20,00%
Examen parcial 2: Ecuaciones diferenciales	4,30	20,00%
Examen parcial 3: Sucesiones y series	4,40	20,00%
Examen final	4,80	25,00%"""


m13 = """Padlet Semana 1 (Prólogo y capítulos 1-3)	5,00	3,33333333333%
Taller 1: Reconociendo la pseudociencia y desinformación en los medios de comunicación	4,55	8,33333333333%
Padlet Semana 2 (Capítulos 4-7)	5,00	3,33333333333%
Padlet Semana 3 (Capítulos 8-11)	5,00	3,33333333333%
Taller 4: ¿Cómo se comparan las seis ciencias de la facultad?	4,69	8,33333333333%
Padlet Semana 4 (Capítulos 12-15)	5,00	3,33333333333%
Taller 2: Pitágoras	5,00	8,33333333333%
Taller 3: En 10 años...	4,80	8,33333333333%
Taller 5: El quehacer científico y sus posibles consecuencias: Andrew Wakefield y el movimiento antivacunas	5,00	8,33333333333%
Padlet Semana 5 (Capítulos 16-19)	5,00	3,33333333333%
Debate	5,00	10,00000000000%
Taller 6: ¿Por qué se retractan los científicos?	4,50	8,33333333333%
Padlet Semana 6 (7) (Capítulo 20 y reflexión final)	5,00	3,33333333333%
Proyecto grupal	4,68	20,00000000000%"""


m14 = """Complementaria MATE 1105, 18: Álgebra Lineal 1	4,87	20,00%
Examen acumulativo 1	4,58333333	20,00%
Examen acumulativo 2	5,00	20,00%
Examen acumulativo 3	5,00	20,00%
Examen final	5,00	20,00%"""


m15 = """TODO"""


m16 = """QUIM 1104, 26: Laboratorio de Química	4,93	30,00%
Examen parcial 1: Nomenclatura y estequeometría	5,00	14,00%
Quiz 1: Ecuaciones molecular, iónica y iónica neta	5,00	2,00%
Examen parcial 2: Estequeometría y Redox	5,00	14,00%
Examen parcial 3	5,00	14,00%
Quiz 2: Equilibrio dinámico	5,00	2,00%
Quiz 3: Soluciones reguladoras, solubilidad y pH	5,00	3,00%
Examen final acumulativo	5,00	21,00%"""


m17 = """Quiz 1	5,00	1,000000%
Quiz 2	4,00	0,000000%
Quiz 2 con bono	5,00	1,000000%
Quiz 3	5,00	1,000000%
Quiz 4	5,00	1,000000%
Quiz 5	5,00	1,000000%
Moodle 1 (Kapitel 1 und 2 - Obligatorisch)	5,00	5,000000%
Moodle 2 (Kapitel 3, 4, und 5 - Obligatorisch) con bono	5,00	5,000000%
Moodle 3  (Kapitel 6, 7, und 8 - Obligatorisch)	5,00	5,000000%
Miniprojekt 1	4,00	5,000000%
Miniprojekt 2	5,00	5,000000%
Miniprojekt 3	5,00	5,000000%
Cartilla 1	5,00	1,666667%
Cartilla 2	5,00	1,666667%
Cartilla final	5,00	1,666667%
Participación y asistencia 1	5,00	5,000000%
Participación y asistencia 2	5,00	5,000000%
Examen parcial 1	4,80	15,000000%
Examen parcial 2	4,90	15,000000%
Examen parcial 3	4,70	20,000000%"""


m18 = """Reto 1	4,58	12,000000%
Examen parcial 1: Complejidades y estructuras de datos lineales	4,50	16,000000%
Reto 2	4,92	12,000000%
Examen parcial 2: Tablas de símbolos	4,75	16,000000%
Reto 3	5,00	14,000000%
Examen parcial 3: Grafos	4,00	16,000000%
Reto 4	4,53	14,000000%"""


m19 = """Tarea 1: Lógica, conjuntos y demostraciones	4,89	4,000000%
Examen parcial 1: Conjuntos e inducción	5,00	20,000000%
Tarea 2: Conjuntos, inducción e inducción fuerte	5,00	4,000000%
Tarea 3: Algoritmos de división y de Euclides, primos y máximo común divisor	5,00	4,000000%
Examen parcial 2: Aritmética modular, congruencias, primos y primos relativos	5,00	20,000000%
Tarea 4: Teorema chino residuos, pequeño teorema Fermat, relaciones y funciones	4,69	4,000000%
Examen parcial 3: Aritmética modular, funciones, relaciones de equivalencia, órdenes	5,00	20,000000%
Tarea 5: cardinalidades infinitas, conteo	4,69	4,000000%
Examen final	5,00	20,000000%"""


m20 = """FISI 1029, 04: Física Experimental 2	4,62	20,000000%
Complementaria FISI 1528, 26: Física 2	5,00	20,000000%
Quiz de opción múltiple semana 2	3,75	3,333333%
Quiz de opción múltiple semana 3	5,00	3,333333%
Quiz de opción múltiple semana 6	5,00	3,333333%
Examen parcial 1 (asincrónico)	5,00	5,000000%
Quiz de opción múltiple semana 7	5,00	3,333333%
Quiz de opción múltiple semana 10	5,00	3,333333%
Examen parcial 2 (sincrónico)	3,85	5,000000%
Quiz de opción múltiple semana 11	5,00	3,333333%
Examen parcial 3 (asincrónico)	4,90	5,000000%
Examen parcial 4 (asincrónico)	5,00	5,000000%
Examen final	4,25	20,000000%"""


m21 = """Complementaria FISI 2526, 01: Métodos Computacionales 1	5,00	25,000000%
Semana 2: Animación en Python	5,00	6,250000%
Semana 3: Derivación - Campo eléctrico	4,00	0,000000%
Semana 4: Interpolación por Newton-Gregory para puntos no equiespaciados	5,00	6,250000%
Semana 5: Cuadratura gaussiana y de Gauss-Laguerre	5,00	6,250000%
Semana 6: Sistemas de ecuaciones lineales, colisión de dos discos rígidos	5,00	6,250000%
Semana 8: Sobrerelajación MonteCarlo	5,00	6,250000%
Semana 7: Mínimos cuadrados y sistemas de ecuaciones no lineales	5,00	6,250000%
Semana 10: Introducción a probabilidad	5,00	6,250000%
Semana 11: Conteo	5,00	6,250000%
Semana 12: Covarianza	5,00	6,250000%
Semana 3: Derivación - Campo eléctrico [con bono]	4,50	6,250000%
Semana 13: Bondad del ajuste	4,95	6,250000%
Exención Examen final: Hidden Markov models	5,00	6,250000%"""


m22 = """TODO"""


m23 = """TODO"""


m24 = """TODO"""


m25 = """TODO"""


m26 = """TODO"""


m27 = """TODO"""


m28 = """Escrito inicial	4,80	15,0000000%
CL1: Hansel y Gretel	4,00	1,0714286%
CL2: Estructuras de Datos	4,00	1,0714286%
CL3: Ordenamiento	5,00	1,0714286%
CL4: Estructuras de Control	5,00	1,0714286%
CL5: Recursión	5,00	1,0714286%
CL6: Abstracción	4,00	1,0714286%
CL7: Lenguajes	5,00	1,0714286%
CLE1: Algorithmic Inequity	5,00	1,0714286%
CLE2: Pensamiento Deductivo (P)	5,00	1,0714286%
CLE3: Pensamiento Inductivo (P)	5,00	1,0714286%
CLE4: Seguridad en automóviles y máquinas	5,00	1,0714286%
CLE5: The Recursive Universe	5,00	1,0714286%
CLE6: Meritocracia	5,00	1,0714286%
CLE7: Select One	5,00	1,0714286%
Ejercicio individual 1	5,00	1,0714286%
Ejercicio individual 2	5,00	1,0714286%
Ejercicio individual 3	5,00	1,0714286%
Ejercicio individual 4	5,00	1,0714286%
Ejercicio individual 5	5,00	1,0714286%
Ejercicio individual 6	5,00	1,0714286%
Ejercicio individual 7	5,00	1,0714286%
Trabajo de aplicación 1	5,00	2,1428571%
Trabajo de aplicación 2	5,00	2,1428571%
Trabajo de aplicación 3	5,00	2,1428571%
Trabajo de aplicación 4	5,00	2,1428571%
Trabajo de aplicación 5	5,00	2,1428571%
Trabajo de aplicación 6	5,00	2,1428571%
Trabajo de aplicación 7	5,00	2,1428571%
Ejercicio grupal 1	5,00	1,0714286%
Ejercicio grupal 2	4,50	1,0714286%
Ejercicio grupal 3	5,00	1,0714286%
Ejercicio grupal 4	5,00	1,0714286%
Ejercicio grupal 5	5,00	1,0714286%
Ejercicio grupal 6	5,00	1,0714286%
Ejercicio grupal 7	5,00	1,0714286%
Ética individual 1	5,00	1,0714286%
Ética individual 2	5,00	1,0714286%
Ética individual 3	5,00	1,0714286%
Ética individual 4	5,00	1,0714286%
Ética individual 5	5,00	1,0714286%
Ética individual 6	5,00	1,0714286%
Ética individual 7	5,00	1,0714286%
Ética grupal 1	5,00	1,0714286%
Ética grupal 2	5,00	1,0714286%
Ética grupal 3	5,00	1,0714286%
Ética grupal 4	5,00	1,0714286%
Ética grupal 5	5,00	1,0714286%
Ética grupal 6	5,00	1,0714286%
Ética grupal 7	5,00	1,0714286%
Video del Ensayo Final	1,00	0,0000000%
Ensayo final	5,00	25,0000000%"""


m29 = """Entrega 1: ¿Qué materia prima usaron los dioses para crear las cosas que hay en el mundo?	5,00	5,0000000%
Entrega 2: ¿Cuál es la diferencia entre un alquimista y un químico?	5,00	6,0000000%
Evaluación Parcial 1	4,58	12,0000000%
Entrega 3: ¿Existe un elemento con el cual se pueden construir todas las cosas existentes?	5,00	7,0000000%
Evaluación Parcial 2	5,00	12,0000000%
Entrega 4: Repensando: ¿Cuál es la diferencia entre un alquimista y un químico?	5,00	8,0000000%
Entrega 5: ¿Qué se necesitó para que la Química se convirtiera en ciencia?	5,00	8,0000000%
Evaluación Parcial 3	4,58	12,0000000%
Actividad 1, quiz: Videos semana 1	5,00	2,8571429%
Actividad 2, quiz: Videos semana 2	4,00	2,8571429%
Actividad 3: Control de lectura	5,00	2,8571429%
Actividad 4, quiz: Video alquimia	5,00	2,8571429%
Actividad 5, quiz: Videos oxígeno y pila voltaica	4,00	2,8571429%
Actividad 6, 8 pares de isómeros de glucosa 	5,00	2,8571429%
Actividad 7, 3 volumenes de hidrógeno y uno de nitrgógeno dan 2 de amoniaco 	5,00	2,8571429%
Evaluación corta 1: El bronce es aleación de cobre y estaño	5,00	2,0000000%
Evaluación corta 2: Valor de pi para egipcios y Washington Irving	5,00	2,0000000%
Evaluación corta 3: Gas pingüe y significado de "flogisto"	5,00	2,0000000%
Evaluación corta 4: Aire desflogisticado (oxígeno) 	5,00	2,0000000%
Evaluación corta 5: Estados de oxidación y Ley de Avogadro	5,00	2,0000000%"""


m30 = """TODO"""


m31 = """Taller 0: Introducción a Java	5,00	1,0000000%
Taller 1: Programación Orientada a Objetos en Java	3,50	2,0000000%
Taller 2: Análisis	3,90	2,0000000%
Proyecto 1, entrega 1 de 3: Análisis	4,25	4,0000000%
Proyecto 1, entrega 2 de 3: Diseño	4,65	4,0000000%
Examen parcial 1	4,80	24,0000000%
Proyecto 1, entrega 3 de 3: Diseño final e implementación	4,70	4,0000000%
Proyecto 2, entrega 1 de 2: Boceto	5,00	2,0000000%
Taller 4: GUIs. Triqui! Mi primer videojuego.	5,00	1,0000000%
Proyecto 2, entrega 2 de 2: Diseño e implementación	5,00	10,0000000%
Taller 5: Patrones	5,00	2,0000000%
Taller 6: Errores y Excepciones	4,75	4,0000000%
Proyecto 3, entrega 1 de 2: Diseño	4,80	6,0000000%
Examen parcial 2	4,90	24,0000000%
Proyecto 3, entrega 2 de 2: Implementación	5,00	10,0000000%"""


m32 = """Parcial 1	5,00	32,5000000%
Parcial 2	4,93	32,5000000%
Trabajo práctico 1	4,70	5,0000000%
Trabajo práctico 2	4,85	5,0000000%
Trabajo práctico 3	5,00	5,0000000%
Trabajo práctico 4	5,00	5,0000000%
Trabajo práctico 5	5,00	10,0000000%
Participación en clase 1 (32 puntos)	5,00	2,5000000%
Participación en clase 2	5,00	2,5000000%"""


m33 = """TODO"""


m34 = """Examen Parcial 1 	4,1	0,0000000%
Examen Parcial 2	4,89	14,0000000%
Examen Parcial 3	4,40	10,0000000%
Ejercicio 1: Fuerzas de Porter	5,00	0,3333333%
Ejercicio BMM	5,00	0,3333333%
Ejercicio Canvas	5,00	0,3333333%
Ejercicio Cadena de Valor Uniandes	5,00	0,3333333%
Quiz en clase	5,00	0,3333333%
Quiz de asistencia	5,00	0,3333333%
Escenario 1	5,00	2,0000000%
Escenario 2	5,00	2,0000000%
Escenario 3: SAP	5,00	2,0000000%
Escenario 4: Power BI	5,00	2,0000000%
Proyecto - P1 Grupal	4,87	9,0000000%
Proyecto - P0 Ejercicio comparación CO 	5,00	3,0000000%
Proyecto - P1 Individual - Plan de texto	4,65	3,0000000%
Proyecto - P1 Individual - Versión inicial	4,68	5,0000000%
Proyecto - P1 Individual - Versión final	5,00	10,0000000%
Proyecto - P2 Grupal	4,85	9,0000000%
Proyecto - P2 Individual - Bibliografía comentada	4,46	5,0000000%
Proyecto - P2 Individual - Versión final	5,00	12,0000000%
0.5 puntos en Parcial 1 por ser estudiante con más bonos (21)	4,60	10,0000000%"""


m35 = """TODO"""


m36 = """TODO"""


m37 = """TODO"""


m38 = """TODO"""


m39 = """TODO"""


m40 = """TODO"""


m41 = """TODO"""


m42 = """TODO"""


m43 = """TODO"""


m44 = """TODO"""


m45 = """TODO"""


m46 = """TODO"""


m47 = """TODO"""


m48 = """TODO"""


m49 = """TODO"""


m50 = """TODO"""


m51 = """Tarea 1	5,00	5,00%
Tarea 2	4,70	5,00%
Tarea 3 y 4	5,00	10,00%
Examen 1 (parte escrita: 4.9; parte computacional: 5.0)	5,00	30,00%
Examen final escrito	4,80	24,50%
Examen final computacional	5,00	10,50%
Exposición del trabajo final	5,00	15,00%"""

# list(map(print, ['m%i = """TODO"""\n\n' % i for i in range(1, 51)]))
# print("["+",".join(['m%i' % i for i in range(1, 52)])+"]")


def organize_data(subject_name, id):
    if subject_name == "TODO":
        return
    subject_name = subject_name.split('\n')
    subject_name = [x.split('\t') for x in subject_name]
    subject_name = [x for x in subject_name if len(x) == 3]
    subject_name = [{"subject_id": id, "name": x[0], "grade": float(x[1].replace(",", ".")), "percentage": int(x[2].split(",")[0])/100} for x in subject_name]
    return subject_name


datos = []
count = 1
for subject in [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,m34,m35,m36,m37,m38,m39,m40,m41,m42,m43,m44,m45,m46,m47,m48,m49,m50,m51]:
    materias_paila = []
    data = organize_data(subject, count)
    count += 1
    if data is not None:
        # print(data)
        # s = input("Datos de la materia %i" % count + "Bien?")
        # if s == "n":
        #     materias_paila.append(count)
        #     continue
        datos += data
        with open('app/data/assignments.json', 'w', encoding="utf-8") as outfile:
            json.dump(datos, outfile, ensure_ascii=False, indent=4)
    continue


