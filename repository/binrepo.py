import pickle

from repository.repo import Repository, GradesRepository


class PickleRepo(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._load()

    def _load(self):
        f = open(self.__file_name, 'rb')
        try:
            items = pickle.load(f)
        except EOFError:
            items = []
        for item in items:
            super().add(item)

    def _save(self):
        f = open(self.__file_name, 'wb')
        pickle.dump(super().get_data(), f)
        f.close()

    def add(self, item):
        super().add(item)
        self._save()

    def remove_item(self, id):
        super().remove_item(id)
        self._save()

    def update(self, id, new_name, element):
        super().update(id, new_name, element)
        self._save()


class GradesPickleRepo(GradesRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self._load()

    def _load(self):
        f = open(self.__file_name, 'rb')
        try:
            items = pickle.load(f)
        except EOFError:
            items = []
        for item in items:
            super().append_grade(item)

    def _save(self):
        f = open(self.__file_name, 'wb')
        pickle.dump(super().get_grades(), f)
        f.close()

    def add(self, student_id, discipline_id, grade_value):
        super().add(student_id, discipline_id, grade_value)
        self._save()

    def delete_by_student(self, student_id):
        super().delete_by_student(student_id)
        self._save()

    def delete_by_discipline(self, discipline_id):
        super().delete_by_discipline(discipline_id)
        self._save()

    def remove_student_grade(self, student_id, discipline_id):
        super().remove_student_grade(student_id, discipline_id)
        self._save()

    def append_grade(self, item):
        super().append_grade(item)
        self._save()


"""
repo = TextRepository('students.txt')
# repo = ['ceva', 'altceva']

def write_bin_file(repo):
    f = open('stud', 'wb')  # read text
    pickle.dump(repo, f)
    f.close()

def read_bin_file():
    f = open('stud', 'rb')  # read text
    repo = pickle.load(f)
    f.close()
    return repo
write_bin_file(repo)
"""

