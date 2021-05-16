class Grades:

    def __init__(self, subject: str, grade_1: float, grade_2: float, grade_3: float, grade_4: float):
        self._subject = subject
        self._grade_1 = grade_1
        self._grade_2 = grade_2
        self._grade_3 = grade_3
        self._grade_4 = grade_4

    def calculate_final_grade(self) -> float:
        final_grade: float

        final_grade = (self._grade_1 + self._grade_2 +
                       self._grade_3 + self._grade_4) / 4

        return final_grade

    @property
    def get_subject(self):
        return self._subject