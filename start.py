import traceback

from commands.validators import Validator
from repository.binrepo import PickleRepo, GradesPickleRepo
from repository.repo import Repository, GradesRepository
from repository.textrepo import TextRepository, GradesTextRepository
from ui.console import Console
from commands.command import StudentCommand, DisciplineCommand, GradesCommand
import pickle
from settings.settings import Settings

if __name__ == '__main__':
    try:
        settings = Settings("settings.properties")

        if settings.get_repo_type() == 'inmemory':
            students_repo = Repository()
            disciplines_repo = Repository()
            grades_repo = GradesRepository()
        elif settings.get_repo_type() == 'text_file':
            students_repo = TextRepository('students.txt')
            disciplines_repo = TextRepository('disciplines.txt')
            grades_repo = GradesTextRepository('grades.txt')
        elif settings.get_repo_type() == 'binaryfiles':
            students_repo = PickleRepo('students.pickle')
            disciplines_repo = PickleRepo('disciplines.pickle')
            grades_repo = GradesPickleRepo('grades.pickle')

        validator = Validator()

        student_command = StudentCommand(students_repo, validator, grades_repo)
        discipline_command = DisciplineCommand(disciplines_repo, grades_repo, validator)
        grades_command = GradesCommand(validator, grades_repo)

        console = Console(student_command, discipline_command, grades_command)
        console.run_menu()


        # repo = TextRepository('students.txt')


        # repo = ['ceva', 'altceva']
        """
        def write_bin_file(students_text_repo):
            f = open('stud.pickle', 'wb')  # read text
            pickle.dump(students_text_repo, f)
            f.close()


        def read_bin_file():
            f = open('stud.pickle', 'rb')  # read text
            smth = pickle.load(f)
            f.close()
            return smth
        """
        # write_bin_file(students_text_repo)
        # print(read_bin_file())
    except AssertionError:
        print("Assertion Error!")
    except Exception as ex:
        print("Unknown error caught: ", ex)
        traceback.print_exc()
