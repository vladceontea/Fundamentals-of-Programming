from entity.grade import Grade
import random

from module import IterableObject


class GradeRepo:

    def __init__(self, discipline_repo, student_repo):
        self._grade_list = IterableObject()
        self._student_repo = student_repo
        self._discipline_repo = discipline_repo

    @property
    def grade_list(self):
        return self._grade_list

    def get_all(self):
        return self._grade_list

    def add_grades_repo(self, add_list):
        for grade in add_list:
            self._grade_list.add(grade)

    def delete_grades_repo(self, delete_list):
        for value in delete_list:
            i = 0
            while i < len(self._grade_list):
                if value == self._grade_list[i]:
                    self._grade_list.__delitem__(i)
                else:
                    i = i + 1

    def add_random_grade(self):
        student_id_list = []
        discipline_id_list = []
        for student in self._student_repo.student_list:
            student_id_list.append(student.student_id)
        for discipline in self._discipline_repo.discipline_list:
            discipline_id_list.append(discipline.discipline_id)

        grade = Grade(random.choice(student_id_list), random.choice(discipline_id_list), random.randint(1, 10))
        self._grade_list.add(grade)

    def delete_student_repo(self, student_id):
        i = 0
        while i < len(self._grade_list):
            if student_id == self._grade_list[i].student_id:
                self._grade_list.__delitem__(i)
            else:
                i = i + 1

    def delete_discipline_repo(self, discipline_id):
        i = 0
        while i < len(self._grade_list):
            if discipline_id == self._grade_list[i].discipline_id:
                self._grade_list.__delitem__(i)
            else:
                i = i + 1

    def average_grade(self, discipline_id, student_id):
        total = 0
        i = 0
        for grade in self._grade_list:
            if grade.student_id == student_id and grade.discipline_id == discipline_id:
                total = total + grade.grade_value
                i = i + 1
        if i == 0:
            return 0
        else:
            return total/i
