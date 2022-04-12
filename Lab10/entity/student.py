
class StudentException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class StudentValidationException(StudentException):
    def __init__(self, error_list):
        self._errors = error_list

    def __str__(self):
        result = ''

        for er in self._errors:
            result += er
            result += '\n'
        return result


class StudentValidator:
    def validate(self, student):
        errors = []
        if len(student.name) < 5:
            errors.append('Student name requires more letters')
        if student.student_id < 100 or student.student_id > 199:
            errors.append('Not a valid student ID')

        if len(errors) > 0:
            raise StudentValidationException(errors)


class Student:

    def __init__(self, student_id=0, name=''):
        """
        Defines the Student type
        :param student_id: The id of the student
        :param name: The name of the student
        """

        if not isinstance(student_id, int):
            raise StudentException('Invalid value for student_id!')
        if not isinstance(name, str):
            raise StudentException('Invalid value for student name!')

        self._student_id = student_id
        self._name = name

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @student_id.setter
    def student_id(self, value):
        self.student_id = value

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return '\033[36m' + 'Student ID: ' + '\033[0m' + str(self._student_id) + '\033[36m' + ' Name: ' + '\033[0m' + self._name.ljust(15)
