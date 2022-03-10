from repository.repo import Repository, GradesRepository


class TextRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add(self, item):
        super().add(item)
        self.save()

    def save(self):
        f = open(self._file_name, 'wt')
        for item in self._data:
            line = str(self._data[item].id) + ' ' + str(self._data[item].name)
            f.write(line)
            f.write('\n')
        f.close()

    def remove_item(self, id):
        super().remove_item(id)
        self.save()

    def update(self, id, new_name, element):
        super().update(id, new_name, element)
        self.save()

    def _load(self):
        f = open(self._file_name, 'rt')
        f.close()


class GradesTextRepository(GradesRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _load(self):
        f = open(self._file_name, 'rt')
        f.close()

    def save(self):
        f = open(self._file_name, 'wt')
        for item in self._grades:
            line = 'student: ' + str(item['student']) + ' ; ' + 'discipline: ' + str(item['discipline']) + \
                   ' ; ' + 'grades: ' + str(item['grades'])
            f.write(line)
            f.write('\n')
        f.close()

    def add(self, student_id, discipline_id, grade_value):
        super().add(student_id, discipline_id, grade_value)
        self.save()

    def delete_by_student(self, student_id):
        super().delete_by_student(student_id)
        self.save()

    def delete_by_discipline(self, discipline_id):
        super().delete_by_discipline(discipline_id)
        self.save()

    def remove_student_grade(self, student_id, discipline_id):
        super().remove_student_grade(student_id, discipline_id)
        self.save()

    def append_grade(self, item):
        super().append_grade(item)
        self.save()
        """
        f = open(self._file_name, 'a')
        line = 'student: ' + str(item['student']) + ' ; ' + 'discipline: ' + str(item['discipline']) + \
               ' ; ' + 'grades: ' + str(item['grades'])
        f.write(line)
        f.write('\n')
        f.close()
        """
        # i = 0
        # while i < len(item):
        #     line = 'student: ' + str(item[i]['student']) + ' ; ' + 'discipline: ' + str(item[i]['discipline']) + \
        #            ' ; ' + 'grades: ' + str(item[i]['grades'])
        #     f.write(line)
        #     f.write('\n')
        #     i += 1
