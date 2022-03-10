from enum import Enum

from repository.repo import GradesRepository


def add_student_handler(student_command, student):
    student_command.remove_student(student.id)
    #student_repo.remove_item(student.id)


def add_discipline_handler(discipline_command, discipline):
    discipline_command.remove_discipline(discipline.id)
    # discipline_repo.remove_item(discipline.id)


def delete_student_handler(student_command, student, grades_command, grades):
    student_command.add_student(student.id, student.name)
    i = 0
    while i < len(grades):
        grades_command.append_item(grades[i])
        i += 1


def delete_discipline_handler(discipline_command, discipline, grades_command, grades):
    discipline_command.add_discipline(discipline.id, discipline.name)
    i = 0
    while i < len(grades):
        grades_command.append_item(grades[i])
        i += 1


def update_student_handler(student_command, student, name):
    student_command.update_student(student.id, name, student)

def update_discipline_handler(discipline_command, discipline, name):
    discipline_command.update_discipline(discipline.id, name, discipline)


def grade_student_handler(grades_command, student_id, discipline_id):
    grades_command.remove_grade(student_id, discipline_id)


def redo_add_student(student_command, student):
    student_command.add_student(student.id, student.name)
    # student_text.add_in_file(student)


def redo_add_discipline(discipline_command, discipline):
    discipline_command.add_discipline(discipline.id, discipline.name)
    # discipline_text.add_in_file(discipline)


def redo_delete_student(student_command, student):
    student_command.remove_student(student.id)
    # students_text.delete(student.id)
    # grades_text.delete_student(student.id)


def redo_delete_discipline(discipline_command, discipline):
    discipline_command.remove_discipline(discipline.id)
    # disciplines_text.delete(discipline.id)
    # grades_text.delete_discipline(discipline.id)


def redo_update_student(student_command, student, name):
    student_command.update_student(student.id, name, student)


def redo_update_discipline(discipline_command, discipline, name):
    discipline_command.update_discipline(discipline.id, name, discipline)


def redo_grade_student(grades_command, student_id, discipline_id, grade_value):
    grades_command.grade_student(student_id, discipline_id, grade_value)


class UndoHandler(Enum):
    ADD_STUDENT = add_student_handler
    ADD_DISCIPLINE = add_discipline_handler
    DELETE_STUDENT = delete_student_handler
    DELETE_DISCIPLINE = delete_discipline_handler
    UPDATE_STUDENT = update_student_handler
    UPDATE_DISCIPLINE = update_discipline_handler
    GRADE_STUDENT = grade_student_handler


class RedoHandler(Enum):
    ADD_STUDENT = redo_add_student
    ADD_DISCIPLINE = redo_add_discipline
    DELETE_STUDENT = redo_delete_student
    DELETE_DISCIPLINE = redo_delete_discipline
    UPDATE_STUDENT = redo_update_student
    UPDATE_DISCIPLINE = redo_update_discipline
    GRADE_STUDENT = redo_grade_student

"""
def add_student_handler(student_command, student_id, student_name, student_text):
    student_command.remove_student(student_id)
    student_text.delete()
"""