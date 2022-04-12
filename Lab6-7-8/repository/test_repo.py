import unittest

from entity.discipline import Discipline
from entity.student import Student

from repository.DisciplineRepo import DisciplineRepo
from repository.StudentRepo import StudentRepo


class TestDisciplineRepo(unittest.TestCase):
    def test_add_random_disciplines(self):
        repo = DisciplineRepo()
        for i in range(10):
            repo.add_random_discipline()
        self.assertEqual(len(repo.discipline_list), 10)

    def test_add_repo(self):
        repo = DisciplineRepo()
        d1 = Discipline(234, 'Algebra')
        d2 = Discipline(245, 'Calculus')
        repo.add_discipline_repo(d1)
        repo.add_discipline_repo(d2)

        self.assertEqual(len(repo.discipline_list), 2)

    def test_remove_repo(self):
        repo = DisciplineRepo()
        d1 = Discipline(234, 'Algebra')
        d2 = Discipline(245, 'Calculus')
        repo.add_discipline_repo(d1)
        repo.add_discipline_repo(d2)

        repo.delete_discipline_repo(245)

        self.assertEqual(len(repo.discipline_list), 1)

    def test_update_repo(self):
        repo = DisciplineRepo()
        d1 = Discipline(234, 'Algebra')
        d2 = Discipline(245, 'Calculus')
        repo.add_discipline_repo(d1)
        repo.add_discipline_repo(d2)

        repo.update_discipline_repo(234, 'Geometry')

        self.assertEqual(repo.discipline_list[0].name, 'Geometry')


class TestStudentRepo(unittest.TestCase):
    def test_add_random_students(self):
        my_list = StudentRepo()
        for i in range(10):
            my_list.add_random_student()
        self.assertEqual(len(my_list.student_list), 10)

    def test_add_repo(self):
        repo = StudentRepo()
        s1 = Student(134, 'John Johnson')
        s2 = Student(145, 'Mike Moody')
        repo.add_student_repo(s1)
        repo.add_student_repo(s2)

        self.assertEqual(len(repo.student_list), 2)

    def test_remove_repo(self):
        repo = StudentRepo()
        s1 = Student(134, 'John Johnson')
        s2 = Student(145, 'Mike Moody')
        repo.add_student_repo(s1)
        repo.add_student_repo(s2)
        repo.delete_student_repo(134)

        self.assertEqual(len(repo.student_list), 1)

    def test_update_repo(self):
        repo = StudentRepo()
        s1 = Student(134, 'John Johnson')
        s2 = Student(145, 'Mike Moody')
        repo.add_student_repo(s1)
        repo.add_student_repo(s2)
        repo.update_student_repo(134, 'Liviu Rebreanu')

        self.assertEqual(repo.student_list[0].name, 'Liviu Rebreanu')
