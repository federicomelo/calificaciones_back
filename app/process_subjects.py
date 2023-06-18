# Python

import json


SUBJECTS = """|1|Consitución|DERE-1300, 11: Constitución y Democracia|
    |1|Diferencial|MATE-1203, 04: Cálculo Diferencial|
    |1|Escritura II|LENG-1512, 36: Escritura Universitaria II (Ciclo 2 de 8 semanas)|
    |1|Escritura I|LENG-1511, 06: Escritura Universitaria I (Ciclo 1 de 8 semanas)|
    |1|Herramientas|DECA-1001, 05: Herramientas para la Vida Universitaria|
    |1|IP|ISIS-1221, 28: Introducción a la Programación|
    |1|Intro a Física|FISI-1502, 01: Introducción a la Física|
    |1|Natación|DEPO-1228, 02: Selección de Natación|
    |2|CBU Colombia|CBCC-1177, 18: Colombia: Espacio, Tiempo y Diferencia (Ciclo 1 de 8 semanas)|
    |2|Filosofía Sueños|CBCA-1329, 01: Filosofía de los Sueños y Adivinación en la Antigüedad|
    |2|Física 1|FISI-1518, 16: Física 1|
    |2|Integral|MATE-1214, 35: Cálculo Integral con Ecuaciones Diferenciales|
    |2|Intro a Ciencias|FCIE-1010, 01: Introducción a las Ciencias (Ciclo 2 de 8 semanas)|
    |2|Lineal 1|MATE-1105, 18: Álgebra Lineal 1|
    |2|Natación|DEPO-1228, 02: Selección de Natación|
    |2|Química|QUIM-1103, 02: Química|
    |3|Alemán 1|LENG-1301, 08: Alemán 1|
    |3|EDA|ISIS-1225, 02: Estructuras de Datos y Algoritmos|
    |3|Estructural|MATE-1102, 01: Matemática Estructural|
    |3|Física 2|FISI-1528, 26: Física 2|
    |3|Métodos 1|FISI-2526, 01: Métodos Computacionales 1|
    |3|Natación|DEPO-1228, 02: Selección de Natación|
    |3|Vecto|MATE-1207, 19: Cálculo Vectorial|
    |4.5|CBU Blues|CBCA 1154, 01: Apreciación de Blues y Rock Clásico|
    |4.5|CBU Casa|CBCA 1012, 01: La Historia de una Casa: Un Relato del Habitar Doméstico en Occidente|
    |4.5|Proba 1|IIND 2106, 02: Probabilidad y Estadística 1|
    |4|Alemán 2|LENG-1302, 02: Alemán 2|
    |4|CBU Pensamiento Comp|CBPC-1176, 01: Introducción al Pensamiento Computacional (Ciclo 1 de 8 semanas) (Épsilon)|
    |4|CBU Química|CBPC-1174, 01: Química, Leyes y Conceptos (Ciclo 1 de 8 semanas)|
    |4|Cupi|ISIS-1211, 01: Cupitaller|
    |4|DPOO|ISIS-1226, 03: Diseño y Programación Orientada a Objetos|
    |4|Infratec|ISIS-1304, 03: Fundamentos de Infraestructura Tecnológica|
    |4|Natación|DEPO-1228, 02: Selección de Natación|
    |4|TI|ISIS-1404, 08: Tecnologías de la Información (TI) en las Organizaciones (Tipo E)|
    |4|Vecto|MATE-1207, 20: Cálculo Vectorial|
    |5|Alemán 3|LENG 1303, 02: Alemán 3|
    |5|CBU Moda|CBCA 1061, 01: Historia del Traje en Occidente (Tipo E)|
    |5|Dalgo|ISIS 1105, 03: Diseño y Análisis de Algoritmos (Dalgo)|
    |5|Desarrollo|ISIS 2603, 03: Desarrollo de Software en Equipos|
    |5|Intro|ISIS 1001, 04: Introducción a la Ingeniería de Sistemas|
    |5|LYM|ISIS 1106, 02: Lenguajes y Máquinas (LYM) (Tipo I)|
    |5|Natación|DEPO-1228, 02: Selección de Natación|
    |5|Sistrans|ISIS 2304, 03: Sistemas Transaccionales (Sistrans)|
    |6|Arquiemp|ISIS 2403, 02: Arquitectura Empresarial (Arquiemp)|
    |6|Arquisoft|ISIS 2503, 02: Arquitectura y Diseño de Software (Arquisoft)|
    |6|Infracomp|ISIS 2203, 01: Infraestructura Computacional (Infracomp)|
    |6|MOS|ISIS 3302, 02: Modelado, Simulación y Optimización (MOS)|
    |6|Natación|DEPO 1228, 02: Selección de Natación|
    |6|PMC|ISIS 2007, 01: Diseño de Productos e Innovación en TI (PMC)|
    |6|CBU Animales|CBCO 1345, 01: El Animal en el Paisaje Colombiano|
    |6|Juegos|MATE 3712, 01: Teoría de Juegos|"""

def process_subjects(subjects=SUBJECTS):
    subjects_iter = iter(subjects.splitlines())
    processed_subjs = map(process_subject, subjects_iter)
    subjs_json = json.dumps(list(processed_subjs), indent=4)
    with open('subjects.json', 'w', encoding="UTF-8") as f:
        f.write(subjs_json)


def process_subject(subject: str) -> dict:
    parts = subject.strip()[1:].split('|')
    semester = float(parts[0])
    abbreviation = parts[1]
    code_name = parts[2]
    code = code_name[:4]
    number = int(code_name[5:9])
    section = int(code_name[11:13])
    name = code_name[15:]
    return {
        'semester': semester,
        'abbreviation': abbreviation,
        'code': code,
        'number': number,
        'section': section,
        'name': name,
        'credits': 3,
        'rounding_policy': 0.01
    }



    


process_subjects()