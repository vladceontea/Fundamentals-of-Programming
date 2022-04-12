from entity.student import Student
from service.UndoService import FunctionCall, Operation


class StudentService:

    def __init__(self, student_repo, student_validator, undo_service):
        self._student_repo = student_repo
        self._student_validator = student_validator
        self._undo_service = undo_service

    @property
    def student_repo(self):
        return self._student_repo

    def add_student(self, student_id, name):
        """
        Adds a student, checking if it has valid values
        :param student_id: The ID of the new student
        :param name: The name of the new student
        :return: -
        """
        student = Student(student_id, name)
        self._student_validator.validate(student)
        self._student_repo.add_student_repo(student)

        undo_function = FunctionCall(self._student_repo.delete_student_repo, student_id)
        redo_function = FunctionCall(self._student_repo.add_student_repo, student)

        self._undo_service.record(Operation(undo_function, redo_function))

    def add_random_student(self):
        """
        Adds a student with randomized parameters
        :return: -
        """
        self._student_repo.add_random_student()

    def delete_student(self, student_id):
        """
        Deletes a student
        :param student_id: The ID of the student
        :return: -
        """
        self._student_repo.delete_student_repo(student_id)

    def update_student(self, student_id, name):
        """
        Updates the name of a student
        :param student_id: The ID of the student
        :param name: The new name of the student
        :return: -
        """
        old_name = ''
        for student in self._student_repo.student_list:
            if student.student_id == student_id:
                old_name = student.name

        student = Student(student_id, name)
        self._student_validator.validate(student)
        self._student_repo.update_student_repo(student_id, name)

        undo_function = FunctionCall(self._student_repo.update_student_repo, student_id, old_name)
        redo_function = FunctionCall(self._student_repo.update_student_repo, student_id, name)

        self._undo_service.record(Operation(undo_function, redo_function))
