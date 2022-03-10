from commands.validators import StoreException
from domain.grades import Grades
import sys

sys.path.insert(1, 'C:\\Users\\Octavia\\Documents\\GitHub\\a10-917OctaviaSuceava')

from main import gnome_sort, compare, reverse_compare, Collection, filter_list


class RepositoryException(StoreException):
    pass


class Repository:
    # def __init__(self):
    #     self._data = {}
    def __init__(self):
        self._data = Collection()
        # self._data = self.transform_to_dict()

    # def transform_to_dict(self):
    #     return {self._data[index].id: self._data[index].name
    #             for index in range(len(self._data))}

    def find_by_id(self, id):
        """
        Checks if the id already exists in the list
        :param id: The id of an item from the list
        :return: None or the id (if it's found)
        """
        if id in self._data:
            return id
        else:
            return None

    def add(self, item):
        """
        Adds <item> in the <_data> dictionary
        :param item: Item from the list
        :return:
        """
        if self.find_by_id(item.id) is not None:
            raise RepositoryException("This id already exists in the list.")
        else:
            self._data[item.id] = item

    def remove_item(self, id):
        """
        Removes from the list the item with the specified id
        :param id: The id of an item from the list
        :return:
        """
        if self.find_by_id(id) is None:
            raise RepositoryException("This id does not exist in the list.")
        for item in self._data:
            if item == id:
                self._data.pop(item)
                return

    def get_items(self):
        """
        :return: The values from the _data dictionary
        """
        return self._data.values()

    def search_by_id(self, id_):
        """
        :param id_:
        :return:
        """
        """for item in self._data:
            if self._data[item] == id_:
                return item"""
        # if id_ in self._data:
        #     return self._data[id_].name, self._data[id_].id
        def filter_id(item):
            if item.id == id_:
                return True
            return False
        # print(filter_list(list(self._data.values()), filter_id))
        return filter_list(list(self._data.values()), filter_id)

    def search_by_name(self, string):
        """
        :param string:
        :return:
        """
        def filter_name(item):
            if item.name.lower().find(string.lower()) != -1:
                return True
            return False
        students = []
        # for idd in self._data:
        #     if self._data[idd].name.find(string) != -1:
        #         students.append({'name': self._data[idd].name, 'id': self._data[idd].id})
        # for idd in self._data:
        # txt = self._data[idd].name.lower()
        # stringlower = string.lower()
        # if txt.find(stringlower) != -1:
        #     students.append({'name': self._data[idd].name, 'id': self._data[idd].id})
        # print(self._data.values())
        # print(filter_list(list(self._data.values()), filter_name))
        return filter_list(list(self._data.values()), filter_name)
        # return students

    def update(self, id, new_name, element):
        """
        Replaces the name of the <element> having the id <id> with <new_name>
        :param id: The id of the element
        :param new_name: The new name we want to replace the old one with
        :param element: Element from the list
        :return:
        """
        if self.find_by_id(id) is None:
            raise RepositoryException("This id does not exist in the list.")
        for item in self._data:
            if item == id:
                element.name = new_name
                return

    def get_data(self):
        return self._data

    def get_length(self):
        return len(self._data)


class GradesRepository:
    def __init__(self):
        self._grades = []

    def add(self, student_id, discipline_id, grade_value):
        grade = Grades(student_id, discipline_id)
        if int(grade_value) <= 0 or int(grade_value) > 10:
            raise GradesRepositoryException("The grade must be in the [1, 10] range.")
        for item in self._grades:
            if item['student'] == student_id and item['discipline'] == discipline_id:
                item['grades'].append(grade_value)
                return
        grade.grades_list.append(grade_value)
        self._grades.append(
            {'student': grade.student_id, 'discipline': grade.discipline_id, 'grades': grade.grades_list})

    def remove_student_grade(self, student_id, discipline_id):
        for item in self._grades:
            if item['student'] == student_id and item['discipline'] == discipline_id:
                item['grades'].pop()
                if not item['grades']:
                    self._grades.remove(item)
                return

    def append_grade(self, item):
        self.get_grades().append(item)

    def get_student_id_grade(self, student_id):
        grades_list = []
        for item in self._grades:
            if item['student'] == student_id:
                grades_list.append(item)
        return grades_list

    def get_discipline_id_grades(self, discipline_id):
        grades_list = []
        for item in self._grades:
            if item['discipline'] == discipline_id:
                grades_list.append(item)
        return grades_list

    def get_avg(self, item):
        return item['avg']

    def order_disciplines(self, disciplines):  # =======================
        average = []
        average_sort = []
        for discipline in disciplines:
            avg = 0
            number = 0
            for grade in self._grades:
                if grade['discipline'] == discipline.id:
                    sum = 0
                    k = 0
                    number += 1
                    for item in grade['grades']:
                        sum += int(item)
                        k += 1
                    sum /= k
                    avg += sum
            if avg != 0:
                avg /= number
                average.append({'id': discipline.id, 'name': discipline.name, 'avg': avg})
        for i in average:
            average_sort.append(i['avg'])
        gnome_sort(average_sort, reverse_compare)
        # average.sort(reverse=True, key=self.get_avg)
        return average, average_sort

    def highest_grades(self, students):  # =============================
        average_grades = []
        average_grades_sort = []
        length = 0
        for student in students:
            avg = 0
            number = 0
            for grade in self._grades:
                if grade['student'] == student.id:
                    sum = 0
                    k = 0
                    number += 1
                    for item in grade['grades']:
                        sum += int(item)
                        k += 1
                    sum /= k
                    avg += sum
            if avg != 0:
                avg /= number
                length += 1
                average_grades.append({'id': student.id, 'name': student.name, 'avg': avg})
        for i in average_grades:
            average_grades_sort.append(i['avg'])
        gnome_sort(average_grades_sort, reverse_compare)
        # average_grades.sort(reverse=True, key=self.get_avg)
        return average_grades, average_grades_sort

    def get_grades(self):
        return self._grades

    def delete_by_student(self, student_id):
        i = 0
        while i < len(self._grades):
            if self._grades[i]['student'] == student_id:
                self._grades.pop(i)
            else:
                i += 1

    def delete_by_discipline(self, discipline_id):
        i = 0
        while i < len(self._grades):
            if self._grades[i]['discipline'] == discipline_id:
                self._grades.pop(i)
            else:
                i += 1

    def failing(self):  # ==============================
        students = []
        for item in self._grades:
            k = 0
            sum = 0
            for i in item['grades']:
                sum += int(i)
                k += 1
            if sum / k < 5:
                students.append(
                    {'student': item['student'], 'discipline': item['discipline'], 'average grade': sum / k})
        return students


class GradesRepositoryException(StoreException):
    pass
