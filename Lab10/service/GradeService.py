from entity.discipline import Discipline
from entity.grade import Grade, GradeException
from entity.student import Student
from service.UndoService import FunctionCall, Operation, CascadedOperation
from module import filter_list, gnome_sort


class GradeService:

    def __init__(self, grade_repo, grade_validator, student_repo, discipline_repo, undo_service):
        self._grade_repo = grade_repo
        self._grade_validator = grade_validator
        self._student_repo = student_repo
        self._discipline_repo = discipline_repo
        self._undo_service = undo_service

    @property
    def grade_repo(self):
        return self._grade_repo

    def create_grade(self, student_id, discipline_id, grade_value):
        student_check = False
        discipline_check = False
        for student in self._student_repo.student_list:
            if student.student_id == student_id:
                student_check = True
        for discipline in self._discipline_repo.discipline_list:
            if discipline.discipline_id == discipline_id:
                discipline_check = True
        if student_check and discipline_check:
            grade = Grade(student_id, discipline_id, grade_value)
            self._grade_validator.validate(grade)
            return grade
        else:
            raise GradeException('The student and/or the discipline does not exist')

    def add_grades(self, add_list):
        self._grade_repo.add_grades_repo(add_list)

        undo_function = FunctionCall(self._grade_repo.delete_grades_repo, add_list)
        redo_function = FunctionCall(self._grade_repo.add_grades_repo, add_list)

        self._undo_service.record(Operation(undo_function, redo_function))

    def add_random_grade(self):
        self._grade_repo.add_random_grade()

    def delete_grades_student(self, student_id):
        delete_list = []
        add_student = Student(0, '')
        for grade in self._grade_repo.grade_list:
            if student_id == grade.student_id:
                delete_list.append(grade)
        for student in self._student_repo.student_list:
            if student_id == student.student_id:
                add_student = student

        self._grade_repo.delete_student_repo(student_id)

        undo_delete_student = FunctionCall(self._student_repo.add_student_repo, add_student)
        redo_delete_student = FunctionCall(self._student_repo.delete_student_repo, student_id)

        undo_delete_grades = FunctionCall(self._grade_repo.add_grades_repo, delete_list)
        redo_delete_grades = FunctionCall(self._grade_repo.delete_grades_repo, delete_list)

        undo_list = []
        redo_list = []

        undo_list.append(undo_delete_student)
        undo_list.append(undo_delete_grades)

        redo_list.append(redo_delete_student)
        redo_list.append(redo_delete_grades)

        self._undo_service.record(CascadedOperation(undo_list, redo_list))

    def delete_grades_discipline(self, discipline_id):
        delete_list = []
        add_discipline = Discipline(0, '')
        for grade in self._grade_repo.grade_list:
            if discipline_id == grade.discipline_id:
                delete_list.append(grade)
        for discipline in self._discipline_repo.discipline_list:
            if discipline_id == discipline.discipline_id:
                add_discipline = discipline

        self._grade_repo.delete_discipline_repo(discipline_id)

        undo_delete_discipline = FunctionCall(self._discipline_repo.add_discipline_repo, add_discipline)
        redo_delete_discipline = FunctionCall(self._discipline_repo.delete_discipline_repo, discipline_id)

        undo_delete_grades = FunctionCall(self._grade_repo.add_grades_repo, delete_list)
        redo_delete_grades = FunctionCall(self._grade_repo.delete_grades_repo, delete_list)

        undo_list = []
        redo_list = []

        undo_list.append(undo_delete_discipline)
        undo_list.append(undo_delete_grades)

        redo_list.append(redo_delete_discipline)
        redo_list.append(redo_delete_grades)

        self._undo_service.record(CascadedOperation(undo_list, redo_list))

    def student_fail(self):
        fail_list = []
        ultimate_list = []
        for student in self._student_repo.student_list:
            for discipline in self._discipline_repo.discipline_list:
                average = self._grade_repo.average_grade(discipline.discipline_id, student.student_id)
                element = [student, average]
                fail_list.append(element)
        fail_list = filter_list(fail_list, self.condition)

        for element in fail_list:
            if element[0] not in ultimate_list:
                ultimate_list.append(element[0])

        return ultimate_list

    def top_students(self):
        average_list = []
        student_list = []
        for student in self._student_repo.student_list:
            total = 0
            i = 0
            for discipline in self._discipline_repo.discipline_list:
                average = self._grade_repo.average_grade(discipline.discipline_id, student.student_id)
                if average != 0:
                    total = total + average
                    i = i + 1
            if i != 0:
                average = total / i
                student_list.append(student)
                average_list.append(average)

        average_list, discipline_list = gnome_sort(average_list, student_list, self.sort_method)

        return student_list, average_list

    def top_disciplines(self):
        average_list = []
        discipline_list = []
        for discipline in self._discipline_repo.discipline_list:
            total = 0
            i = 0
            for student in self._student_repo.student_list:
                average = self._grade_repo.average_grade(discipline.discipline_id, student.student_id)
                if average != 0:
                    total = total + average
                    i = i + 1
            if i != 0:
                average = total / i
                discipline_list.append(discipline)
                average_list.append(average)
        average_list, discipline_list = gnome_sort(average_list, discipline_list, self.sort_method)

        return discipline_list, average_list

    @staticmethod
    def sort_method(a, b):
        return a <= b

    @staticmethod
    def condition(element):
        return 1 <= element < 5
