import random
import traceback

from commands.handlers import UndoHandler, RedoHandler
from commands.undo import UndoManager


class Console:
    def __init__(self, student_command, discipline_command, grades_command):
        self.__student_command = student_command
        self.__discipline_command = discipline_command
        self.__grades_command = grades_command

    def print_menu(self):
        print("\nChoose an option:\n"
              "     > add <student/discipline>\n"
              "     > list <students/disciplines/grades>\n"
              "     > remove <student/discipline>\n"
              "     > update <student/discipline> <id>\n"
              "     > grade <student_id> <discipline_id> <grade_value>\n"
              "     > search <student/discipline> <id/name>\n"
              "     > create statistics\n"
              "     > undo\n"
              "     > redo\n"
              "     > exit\n")

    def statistics_menu(self):
        print("Choose an option:\n"
              "  1 - students failing one or more disciplines\n"
              "  2 - students with the best school situation\n"
              "  3 - all disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students\n")

    def print_students(self):
        """
        Prints the list of students
        :return:
        """
        pos = 0
        for student in self.__student_command.get_students_repo():
            print(pos, ':', student.id, student.name)
            pos += 1

    def print_disciplines(self):
        """
        Prints the list of disciplines
        :return:
        """
        pos = 0
        for discipline in self.__discipline_command.get_disciplines_repo():
            print(pos, ':', discipline.id, discipline.name)
            pos += 1

    def print_grades(self):
        """
        Prints the list of grades
        :return:
        """
        for element in self.__grades_command.get_student_grades():
            print(element)

    def get_avg(self, item):
        return item['avg']

    def print_highest_grades(self, average_grades, average_grades_sorted):
        for item in average_grades_sorted:
            for element in average_grades:
                if element['avg'] == item:
                    print(element['id'], ',', element['name'], ',', element['avg'])

    def search_student(self, string):
        students = self.__student_command.search_student_by_name(string)
        for student in students:
            print(student.name, student.id)
            # print(student['name'], student['id'])

    def search_discipline(self, string):
        disciplines = self.__discipline_command.search_discipline_by_name(string)
        for discipline in disciplines:
            print(discipline.name, discipline.id)

    def search_student_id(self, id_):
        students = self.__student_command.search_student_by_id(id_)
        for student in students:
            print(student.name, student.id)

    def search_discipline_id(self, id_):
        disciplines = self.__discipline_command.search_discipline_by_id(id_)
        for discipline in disciplines:
            print(discipline.name, discipline.id)

    def print_students_failing(self):
        students = self.__grades_command.get_students_failing()
        for student in students:
            print(student['student'], 'is failing at', student['discipline'], 'with an average grade of', student['average grade'])

    def ten_elements(self):
        """
        Adds 10 elements in both students and disciplines list before running the program
        :return:
        """
        number = 0
        disciplines = ["Algebra", "Analysis", "Geography", "History", "English", "Physics", "Geometry", \
                       "Computational Logic", "Fundamentals of Programming", "Economics"]
        students = ["Ana", "Alina", "Andreea", "Alin", "Andrei", "Monica", "Rares", "Razvan", "Alexandru", "Alexandra"]
        while number < 10:
            self.__student_command.add_student(str(random.randrange(1, 700)), students[number])
            for student in self.__student_command.get_students_repo():
                pass
            # self.__students_text_repo.add_in_file(student)
            self.__discipline_command.add_discipline(str(random.randrange(1, 700)), disciplines[number])
            for discipline in self.__discipline_command.get_disciplines_repo():
                pass
            # self.__disciplines_text_repo.add_in_file(discipline)
            number += 1

    def run_menu(self):
        self.ten_elements()
        print("Hello!")
        while True:
            self.print_menu()
            option = input("Your option is: ")
            option = option.strip()
            try:
                if option == 'exit':
                    return
                option = option.split(" ")
                if option[0] == 'add':
                    if option[1] == 'student':
                        id = input("the id is: ")
                        name = input("the name is: ")
                        self.__student_command.add_student(id, name)
                        # self.__students_text_repo.add(self.__student_command.get_student_by_id(id))
                        UndoManager.register_operation(self.__student_command, UndoHandler.ADD_STUDENT,
                                                       self.__student_command.get_student_by_id(id))
                        UndoManager.register_redo(self.__student_command, RedoHandler.ADD_STUDENT,
                                                  self.__student_command.get_student_by_id(id))
                    elif option[1] == 'discipline':
                        id = input("the id is: ")
                        name = input("the name is: ")
                        self.__discipline_command.add_discipline(id, name)
                        # self.__disciplines_text_repo.add(self.__discipline_command.get_discipline_by_id(id))
                        UndoManager.register_operation(self.__discipline_command, UndoHandler.ADD_DISCIPLINE,
                                                       self.__discipline_command.get_discipline_by_id(id))
                        UndoManager.register_redo(self.__discipline_command, RedoHandler.ADD_DISCIPLINE,
                                                  self.__discipline_command.get_discipline_by_id(id))
                elif option[0] == 'list':
                    if option[1] == 'students':
                        self.print_students()
                    elif option[1] == 'disciplines':
                        self.print_disciplines()
                    elif option[1] == 'grades':
                        self.print_grades()
                elif option[0] == 'remove':
                    if option[1] == 'student':
                        id = input("the id is: ")
                        UndoManager.register_operation(self.__student_command, UndoHandler.DELETE_STUDENT, self.__student_command.get_student_by_id(id),
                                                       self.__grades_command,
                                                       self.__grades_command.get_student_grade_by_id(id))
                        UndoManager.register_redo(self.__student_command, RedoHandler.DELETE_STUDENT, self.__student_command.get_student_by_id(id))
                        self.__student_command.remove_student(id)
                        # self.__students_text_repo.remove_item(id)
                        # self.__grades_text_repo.delete_student(id)
                    elif option[1] == 'discipline':
                        id = input("the id is: ")
                        UndoManager.register_operation(self.__discipline_command, UndoHandler.DELETE_DISCIPLINE,
                                                       self.__discipline_command.get_discipline_by_id(id),
                                                       self.__grades_command, self.__grades_command.get_grades_by_discipline(id))
                        UndoManager.register_redo(self.__discipline_command, RedoHandler.DELETE_DISCIPLINE,
                                                  self.__discipline_command.get_discipline_by_id(id))
                        self.__discipline_command.remove_discipline(id)
                        #self.__disciplines_text_repo.remove_item(id)
                        #self.__grades_text_repo.delete_discipline(id)
                elif option[0] == 'update':
                    if option[1] == 'student':
                        new_name = input("the new name of this student is: ")
                        UndoManager.register_operation(self.__student_command, UndoHandler.UPDATE_STUDENT,
                                                       self.__student_command.get_student_by_id(option[2]),
                                                       self.__student_command.get_student_by_id(option[2]).name)
                        self.__student_command.update_student(option[2], new_name,
                                                              self.__student_command.get_student_by_id(option[2]))
                        #self.__students_text_repo.update(option[2], new_name,
                                                              #self.__student_command.get_student_by_id(option[2]))
                        UndoManager.register_redo(self.__student_command, RedoHandler.UPDATE_STUDENT,
                                                  self.__student_command.get_student_by_id(option[2]),
                                                  self.__student_command.get_student_by_id(option[2]).name)
                    else:
                        new_name = input("the new name of this discipline is: ")
                        UndoManager.register_operation(self.__discipline_command, UndoHandler.UPDATE_DISCIPLINE,
                                                       self.__discipline_command.get_discipline_by_id(option[2]),
                                                       self.__discipline_command.get_discipline_by_id(option[2]).name)
                        self.__discipline_command.update_discipline(option[2], new_name,
                                                                    self.__discipline_command.get_discipline_by_id(option[2]))
                        # self.__disciplines_text_repo.update(option[2], new_name,
                        #                                             self.__discipline_command.get_discipline_by_id(option[2]))
                        UndoManager.register_redo(self.__discipline_command, RedoHandler.UPDATE_DISCIPLINE,
                                                       self.__discipline_command.get_discipline_by_id(option[2]),
                                                       self.__discipline_command.get_discipline_by_id(option[2]).name)
                elif option[0] == 'grade':
                    student_id = option[1]
                    discipline_id = option[2]
                    grade_value = option[3]
                    self.__grades_command.grade_student(student_id, discipline_id, grade_value)
                    # self.__grades_text_repo.add_in_file(student_id, discipline_id, grade_value)
                    UndoManager.register_redo(self.__grades_command, RedoHandler.GRADE_STUDENT, student_id, discipline_id, grade_value)
                    UndoManager.register_operation(self.__grades_command, UndoHandler.GRADE_STUDENT, student_id, discipline_id)
                elif option[0] == 'search':
                    if option[1] == 'student':
                        if option[2].isnumeric():
                            self.search_student_id(option[2])
                            # print(self.__student_command.search_student_by_id(option[2]))
                        else:
                            self.search_student(option[2])
                    elif option[1] == 'discipline':
                        if option[2].isnumeric():
                            self.search_discipline_id(option[2])
                            # print(self.__discipline_command.search_discipline_by_id(option[2]))
                        else:
                            self.search_discipline(option[2])
                elif option[0] == 'create' and option[1] == 'statistics':
                    self.statistics_menu()
                    option = input("Your option is: ")
                    if option == '1':
                        self.print_students_failing()
                    elif option == '2':
                        self.print_highest_grades(*self.__grades_command.get_highest_grades(self.__student_command.get_students_repo()))
                    elif option == '3':
                        self.print_highest_grades(*self.__grades_command.get_disciplines_grades(self.__discipline_command.get_disciplines_repo()))
                elif option[0] == 'undo':
                    UndoManager.undo()
                elif option[0] == 'redo':
                    """if UndoManager.get_undo_operations()[len(UndoManager.get_undo_operations()) - 1].handler == UndoHandler.ADD_STUDENT:
                        self.__student_command.add_student('2', 'merge!!!')
                    if UndoManager.redo().handler == UndoHandler.ADD_STUDENT:
                        self.__student_command.add_student(UndoManager.redo().args[0], UndoManager.redo().args[1])"""
                    UndoManager.redo()
                    # if UndoManager.redo().handler == UndoHandler.ADD_STUDENT:
                    #     UndoManager.get_undo_operations().append()
                    # print(UndoManager.get_redo_operations())
                    # print(UndoManager.get_undo_operations())
                else:
                    print("That option does not exist.")
            except Exception as ex:
                print("Error caught: ", ex)
                traceback.print_exc()
