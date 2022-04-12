from entity.student import Student
from repository.StudentRepo import StudentRepo


class StudentRepoText(StudentRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wt')
        student_list = StudentRepo.get_all(self)
        try:
            for student in student_list:
                student_str = str(student.student_id) + ";" + student.name + ";"
                f.write(student_str)
                f.write("\n")
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def _load(self):
        f = open(self._file_name, 'rt')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            student = Student(int(line[0]), line[1])
            super().add_student_repo(student)

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
