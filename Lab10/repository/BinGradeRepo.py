import pickle
from repository.GradeRepo import GradeRepo


class GradeRepoBin(GradeRepo):

    def __init__(self, discipline_repo, student_repo, file_name):
        GradeRepo.__init__(self, discipline_repo, student_repo)
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wb')
        grade_list = GradeRepo.get_all(self)
        pickle.dump(grade_list, f)
        f.close()

    def _load(self):
        try:
            f = open(self._file_name, 'rb')
            self._grade_list = pickle.load(f)
        except EOFError:
            return []

    def add_grades_repo(self, add_list):
        super().add_grades_repo(add_list)
        self._save()

    def delete_grades_repo(self, delete_list):
        super().delete_grades_repo(delete_list)
        self._save()

    def delete_student_repo(self, student_id):
        super().delete_student_repo(student_id)
        self._save()

    def add_random_grade(self):
        super().add_random_grade()
        self._save()

    def delete_discipline_repo(self, discipline_id):
        super().delete_discipline_repo(discipline_id)
        self._save()
