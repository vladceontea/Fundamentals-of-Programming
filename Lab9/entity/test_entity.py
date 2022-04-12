import unittest

from entity.discipline import Discipline, DisciplineValidator, DisciplineValidationException
from entity.student import Student, StudentValidator, StudentValidationException


class TestDiscipline(unittest.TestCase):

    def test_discipline(self):
        discipline1 = Discipline(234, 'Physics')
        self.assertEqual(234, discipline1.discipline_id)
        self.assertEqual('Physics', discipline1.name)

    def test_discipline_validator(self):
        try:
            discipline1 = Discipline(298, 'Physics')
            dv = DisciplineValidator()
            dv.validate(discipline1)
        except DisciplineValidationException as e:
            print(e)


class TestStudent(unittest.TestCase):

    def test_student(self):
        student1 = Student(176, 'Ion Glanetasul')
        self.assertEqual(176, student1.student_id)
        self.assertEqual('Ion Glanetasul', student1.name)

    def test_student_validator(self):
        try:
            student1 = Student(102, 'Maria Pop')
            sv = StudentValidator()
            sv.validate(student1)
        except StudentValidationException as e:
            print(e)
