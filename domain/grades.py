class Grades:
    def __init__(self, student_id, discipline_id):
        self._student_id = student_id
        self._discipline_id = discipline_id
        self._grades_list = []

    @property
    def student_id(self):
        return self._student_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def grades_list(self):
        return self._grades_list