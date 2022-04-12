from entity.grade import Grade
from repository.GradeRepo import GradeRepo


class GradeRepoText(GradeRepo):

    def __init__(self, discipline_repo, student_repo, file_name):
        GradeRepo.__init__(self, discipline_repo, student_repo)
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wt')
        grade_list = GradeRepo.get_all(self)
        try:
            for grade in grade_list:
                grade_str = str(grade.student_id) + ";" + str(grade.discipline_id) + ";" + str(grade.grade_value)
                f.write(grade_str)
                f.write("\n")
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def _load(self):
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()
        add_list = []
        for line in lines:
            line = line.split(';')
            grade = Grade(int(line[0]), int(line[1]), int(line[2]))
            add_list.append(grade)
        super().add_grades_repo(add_list)

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
