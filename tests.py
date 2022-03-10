import unittest
from domain.student import Student
from repository.repo import Repository, GradesRepository

class TestAdd(unittest.TestCase):
    def test_add(self):
        command = Repository()
        command.add(Student(123, "Crina"))
        command.add(Student(901, "Mihai"))
        self.assertEqual(command.get_length(), 2)

class TestRemove(unittest.TestCase):
    def test_remove(self):
        command = Repository()
        command.add(Student(123, "Crina"))
        command.add(Student(901, "Mihai"))
        command.remove_item(901)
        self.assertEqual(command.get_length(), 1)

class TestGrade(unittest.TestCase):
    def test_grade(self):
        grades = GradesRepository()
        grades.add(12, 34, 10)
        try:
            self.assertFalse(grades.add(67, 89, 11))
        except Exception:
            assert True

class TestUpdate(unittest.TestCase):
    def test_update(self):
        command = Repository()
        student = Student(100, "Daria")
        command.add(Student(123, "Crina"))
        command.add(Student(901, "Mihai"))
        try:
            self.assertFalse(command.update(10, "Ioana", student))
        except Exception:
            assert True

if __name__ == '__main__':
    unittest.main()

"""
from domain.student import Student
from repository.repo import Repository, GradesRepository


def test_add():
    command = Repository()
    command.add(Student(123, "Crina"))
    command.add(Student(901, "Mihai"))
    assert command.get_length() == 2

def test_remove():
    command = Repository()
    command.add(Student(123, "Crina"))
    command.add(Student(901, "Mihai"))
    command.remove_item(901)
    assert command.get_length() == 1

def test_grade():
    grades = GradesRepository()
    grades.add(12, 34, 10)
    try:
        grades.add(67, 89, 11)
        assert False
    except Exception:
        assert True

def test_update():
    command = Repository()
    student = Student(100, "Daria")
    command.add(Student(123, "Crina"))
    command.add(Student(901, "Mihai"))
    try:
        command.update(10, "Ioana", student)
        assert False
    except Exception:
        assert True

def test_all():
    test_add()
    test_remove()
    test_grade()
    test_update()"""