
class GradeException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class GradeValidationException(GradeException):
    def __init__(self, error_list):
        self._errors = error_list

    def __str__(self):
        result = ''

        for er in self._errors:
            result += er
            result += '\n'
        return result


class GradeValidator:
    def validate(self, grade):
        errors = []
        if grade.grade_value < 1 or grade.grade_value > 10:
            errors.append('Grade value is not valid')
        if grade.student_id < 100 or grade.student_id > 199:
            errors.append('Not a valid student ID')
        if grade.discipline_id < 200 or grade.discipline_id > 299:
            errors.append('Not a valid discipline ID')

        if len(errors) > 0:
            raise GradeValidationException(errors)


class Grade:

    def __init__(self, student_id=0, discipline_id=0, grade_value=0):
        """
        Defines the Grade type
        :param student_id: The id of the student having the grade
        :param discipline_id: The id of the discipline at which the grade was given
        :param grade_value: The numerical value of the grade
        """

        if not isinstance(student_id, int):
            raise GradeException('Invalid value for student_id')
        if not isinstance(discipline_id, int):
            raise GradeException('Invalid value for discipline_id')
        if not isinstance(grade_value, int):
            raise GradeException('Invalid value for grade_value')

        self._student_id = student_id
        self._discipline_id = discipline_id
        self._grade_value = grade_value

    @property
    def student_id(self):
        return self._student_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def grade_value(self):
        return self._grade_value

    @student_id.setter
    def student_id(self, value):
        self.student_id = value

    @discipline_id.setter
    def discipline_id(self, value):
        self.discipline_id = value

    @grade_value.setter
    def grade_value(self, value):
        self._grade_value = value

    def __str__(self):
        return '\033[35m' + 'Student ID: ' + '\033[0m' + str(self._student_id) + '\033[35m' + ' Discipline ID: ' + '\033[0m' + str(self._discipline_id) + '\033[35m' + ' Value: ' + '\033[0m' + str(self._grade_value)
