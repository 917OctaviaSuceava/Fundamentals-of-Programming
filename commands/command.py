
from domain.student import Student
from domain.discipline import Discipline

class DisciplineCommand:
    def __init__(self, disciplines_repo, grades_repo, validator):
        self.__disciplines_repo = disciplines_repo
        self.__grades_repo = grades_repo
        self.__validator = validator

    def add_discipline(self, discipline_id, name):
        self.__validator.validate_add(discipline_id)
        discipline = Discipline(discipline_id, name)
        self.__disciplines_repo.add(discipline)

    def remove_discipline(self, discipline_id):
        self.__validator.validate_remove(discipline_id, self.__disciplines_repo.get_items())
        self.__disciplines_repo.remove_item(discipline_id)
        self.__grades_repo.delete_by_discipline(discipline_id)

    def get_disciplines_repo(self):
        return self.__disciplines_repo.get_items()

    def get_discipline_by_id(self, id):
        for discipline in self.get_disciplines_repo():
            if discipline.id == id:
                return discipline

    def search_discipline_by_name(self, discipline_name):
        return self.__disciplines_repo.search_by_name(discipline_name)

    def search_discipline_by_id(self, discipline_id):
        return self.__disciplines_repo.search_by_id(discipline_id)

    def update_discipline(self, id, new_name, discipline):
        return self.__disciplines_repo.update(id, new_name, discipline)

class StudentCommand:
    def __init__(self, students_repo, validator, grades_repo):
        self.__students_repo = students_repo
        self.__validator = validator
        self.__grades_repo = grades_repo

    def search_student_by_id(self, student_id):
        return self.__students_repo.search_by_id(student_id)

    def search_student_by_name(self, student_name):
        return self.__students_repo.search_by_name(student_name)

    def add_student(self, student_id, name):
        self.__validator.validate_add(student_id)
        student = Student(student_id, name)
        self.__students_repo.add(student)

    def remove_student(self, student_id):
        self.__validator.validate_remove(student_id, self.__students_repo.get_items())
        self.__students_repo.remove_item(student_id)
        self.__grades_repo.delete_by_student(student_id)

    def get_students_repo(self):
        return self.__students_repo.get_items()

    def get_student_by_id(self, id):
        for student in self.get_students_repo():
            if student.id == id:
                return student

    def get_student_name(self, id):
        for student in self.get_students_repo():
            if student.id == id:
                return student.name

    def update_student(self, id, new_name, student):
        return self.__students_repo.update(id, new_name, student)


class GradesCommand:
    def __init__(self, validator, grades_repo):
        self.__validator = validator
        self.__grades_repo = grades_repo

    def grade_student(self, student_id, discipline_id, grade_value):
        self.__validator.validate_grade(grade_value)
        self.__grades_repo.add(student_id, discipline_id, grade_value)

    def get_student_grades(self):
        return self.__grades_repo.get_grades()

    def append_item(self, item):
        return self.__grades_repo.append_grade(item)

    def get_student_grade_by_id(self, student_id):
        return self.__grades_repo.get_student_id_grade(student_id)

    def get_grades_by_discipline(self, discipline_id):
        return self.__grades_repo.get_discipline_id_grades(discipline_id)

    def get_students_failing(self):
        return self.__grades_repo.failing()

    def get_highest_grades(self, students):
        return self.__grades_repo.highest_grades(students)

    def get_disciplines_grades(self, disciplines):
        return self.__grades_repo.order_disciplines(disciplines)

    def remove_grade(self, student_id, discipline_id):
        return self.__grades_repo.remove_student_grade(student_id, discipline_id)
