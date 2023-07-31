from json import load

SUBJECTS: dict = load(open('app/data/subjects.json'))
SEMESTERS: dict = load(open('app/data/semesters.json'))
ASSIGNMENTS: dict = load(open('app/data/assignments.json'))