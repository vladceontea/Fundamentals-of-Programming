import unittest

from entity.discipline import DisciplineValidator
from entity.student import StudentValidator

from repository.DisciplineRepo import DisciplineRepo
from repository.StudentRepo import StudentRepo

from service.DisciplineService import DisciplineService
from service.StudentService import StudentService


class TestDisciplineService(unittest.TestCase):

    def test_add_random_disciplines(self):
        repo = DisciplineRepo()
        valid = DisciplineValidator()
        service = DisciplineService(repo, valid)
        for i in range(10):
            service.add_random_discipline()
        self.assertEqual(len(service._discipline_repo.discipline_list), 10)

    def test_add(self):
        repo = DisciplineRepo()
        valid = DisciplineValidator()
        service = DisciplineService(repo, valid)
        service.add_discipline(234, 'Algebra')
        service.add_discipline(245, 'Calculus')

        self.assertEqual(len(service._discipline_repo.discipline_list), 2)

    def test_remove(self):
        repo = DisciplineRepo()
        valid = DisciplineValidator()
        service = DisciplineService(repo, valid)
        service.add_discipline(234, 'Algebra')
        service.add_discipline(245, 'Calculus')

        service.delete_discipline(245)

        self.assertEqual(len(service._discipline_repo.discipline_list), 1)

    def test_update(self):
        repo = DisciplineRepo()
        valid = DisciplineValidator()
        service = DisciplineService(repo, valid)
        service.add_discipline(234, 'Algebra')
        service.add_discipline(245, 'Calculus')

        service.update_discipline(234, 'Geometry')

        self.assertEqual(service._discipline_repo.discipline_list[0].name, 'Geometry')


class TestStudentService(unittest.TestCase):

    def test_add_random_students(self):
        repo = StudentRepo()
        valid = StudentValidator()
        service = StudentService(repo, valid)
        for i in range(10):
            service.add_random_student()
        self.assertEqual(len(service._student_repo.student_list), 10)

    def test_add(self):
        repo = StudentRepo()
        valid = StudentValidator()
        service = StudentService(repo, valid)
        service.add_student(134, 'John Johnson')
        service.add_student(145, 'Mike Moody')

        self.assertEqual(len(service._student_repo.student_list), 2)

    def test_remove(self):
        repo = StudentRepo()
        valid = StudentValidator()
        service = StudentService(repo, valid)
        service.add_student(134, 'John Johnson')
        service.add_student(145, 'Mike Moody')

        service.delete_student(145)

        self.assertEqual(len(service._student_repo.student_list), 1)

    def test_update(self):
        repo = StudentRepo()
        valid = StudentValidator()
        service = StudentService(repo, valid)
        service.add_student(134, 'John Johnson')
        service.add_student(145, 'Mike Moody')

        service.update_student(134, 'Liviu Rebreanu')

        self.assertEqual(service._student_repo.student_list[0].name, 'Liviu Rebreanu')
