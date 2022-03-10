class Settings:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__repository = ''
        self.__students = ''
        self.__grades = ''
        self.__text = self.__read_text()

    def __read_text(self):
        information = []
        f = open(self.__file_name, 'r')
        for line in f:
            if '"' in line:
                info = line.split('"')
                file = info[1].strip()
                information.append(file)
            else:
                if '=' in line:
                    info = line.split('=')
                    repo_type = info[1].strip()
                    information.append(repo_type)
        return information

    def get_repo_type(self):
        return self.__text[0]

    def get_students_file(self):
        return self.__text[1]

    def get_disciplines_file(self):
        return self.__text[2]

    def get_grades_file(self):
        return self.__text[3]