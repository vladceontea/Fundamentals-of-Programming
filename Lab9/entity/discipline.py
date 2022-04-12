
class DisciplineException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg


class DisciplineValidationException(DisciplineException):
    def __init__(self, error_list):
        self._errors = error_list

    def __str__(self):
        result = ''

        for er in self._errors:
            result += er
            result += '\n'
        return result


class DisciplineValidator:
    def validate(self, discipline):
        errors = []
        if len(discipline.name) < 3:
            errors.append('Discipline name requires more letters')
        if discipline.discipline_id < 200 or discipline.discipline_id > 299:
            errors.append('Not a valid discipline ID')

        if len(errors) > 0:
            raise DisciplineValidationException(errors)


class Discipline:

    def __init__(self, discipline_id=0, name=''):
        """
        Defines the Discipline type
        :param discipline_id: The id of the discipline
        :param name: The name of the discipline
        """

        if not isinstance(discipline_id, int):
            raise DisciplineException('Invalid value for discipline_id!')
        if not isinstance(name, str):
            raise DisciplineException('Invalid value for discipline name!')

        self._discipline_id = discipline_id
        self._name = name

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def name(self):
        return self._name

    @discipline_id.setter
    def discipline_id(self, value):
        self.discipline_id = value

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return '\033[31m' + 'Discipline ID: ' + '\033[0m' + str(self._discipline_id) + '\033[31m' + ' Name: ' + '\033[0m' + self._name.ljust(22)
