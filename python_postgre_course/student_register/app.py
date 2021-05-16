from models.student import Student
from models.grades import Grades
from typing import List


class App:

    def run(self):
        values: List
        grades: Grades
        student: Student
        name: dict
        address: str
        subejct: str

        address = input('Put your address: ')
        subejct = input('Input the subejct of your study: ')

        name = self.take_name()
        student = Student(name=name['first'], surname=name['surname'], address=address)
        values = self.take_grades()
        grades = Grades(subject=subejct, grade_1=values[0], grade_2=values[1],
                        grade_3=values[2], grade_4=values[3])

        student.set_grades(grades)
        self.print_values(student)

        return 0


    @staticmethod
    def take_name() -> dict:
        name: dict
        name = {
            'first': str(input('Put your first name: ')),
            'surname': str(input('Put your surname: '))
        }

        return name


    @staticmethod
    def take_grades() -> List:
        values = []
        numbers: float

        for i in range(4):
            numbers = float(input(f'input your {i + 1} grade: '))
            values.append(numbers)
            i += 1

        return values


    @staticmethod
    def print_values(student: Student):
        print(f'Name:{student.name} {student.surname}')
        print(student.grades.get_subject, 'total: %.2f' % student.grades.calculate_final_grade())
