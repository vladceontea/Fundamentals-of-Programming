import pickle
from repository.StudentRepo import StudentRepo


class StudentRepoBin(StudentRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wb')
        student_list = StudentRepo.get_all(self)
        pickle.dump(student_list, f)
        f.close()

    def _load(self):
        try:
            f = open(self._file_name, 'rb')
            self._student_list = pickle.load(f)
        except EOFError:
            return []

    def add_student_repo(self, student):
        super().add_student_repo(student)
        self._save()

    def delete_student_repo(self, student_id):
        super().delete_student_repo(student_id)
        self._save()

    def update_student_repo(self, student_id, name):
        super().update_student_repo(student_id, name)
        self._save()

    def add_random_student(self):
        super().add_random_student()
        self._save()
