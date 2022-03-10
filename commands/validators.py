
class StoreException(Exception):
    pass

class Validator:
    def validate_add(self, id_):
        if not id_.isnumeric():
            raise ValueError("The ID must be a number.")

    def validate_grade(self, grade_value):
        if int(grade_value) <= 0 or int(grade_value) > 10:
            raise ValueError("The grade must be in the [1, 10] range.")

    def validate_remove(self, id_, some_list):
        for item in some_list:
            if item.id == id_:
                return
        raise ValueError("That ID does not exist in the list.")
