from models.grades import Grades


class Student:
    _grades: Grades

    def __init__(self, name: str, surname: str, address: str):
        self._name = name
        self._surname = surname
        self._address = address

    def set_grades(self, grades: Grades):
        self._grades = grades

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def grades(self):
        return self._grades
