from repository.BinDisciplineRepo import DisciplineRepoBin
from repository.BinGradeRepo import GradeRepoBin
from repository.BinStudentRepo import StudentRepoBin
from repository.DisciplineRepo import DisciplineRepo
from repository.StudentRepo import StudentRepo
from repository.GradeRepo import GradeRepo
from entity.discipline import DisciplineValidator
from entity.student import StudentValidator
from entity.grade import GradeValidator
from repository.TextDisciplineRepo import DisciplineRepoText
from repository.TextGradeRepo import GradeRepoText
from repository.TextStudentRepo import StudentRepoText
from service.StudentService import StudentService
from service.DisciplineService import DisciplineService
from service.GradeService import GradeService
from service.UndoService import UndoService
from ui.console import MenuUI


def settings():
    file = open('settings.properties', 'rt')
    lines = file.readlines()
    file.close()
    repository = ''
    student_file = ''
    discipline_file = ''
    grade_file = ''
    for line in lines:
        line = line.split(' ')
        if line[0] != '#' and line[0] != '#\n':
            if line[1] == '=':
                if line[0] == 'repository':
                    repository = line[2]
                if line[0] == 'student_file':
                    student_file = line[2]
                if line[0] == 'discipline_file':
                    discipline_file = line[2]
                if line[0] == 'grade_file':
                    grade_file = line[2]

    repository = repository.split('\'')

    student_file = student_file.split('\'')
    discipline_file = discipline_file.split('\'')
    grade_file = grade_file.split('\'')

    if repository[1] == 'inmemory':
        student_repo = StudentRepo()
        discipline_repo = DisciplineRepo()
        grade_repo = GradeRepo(discipline_repo, student_repo)
    elif repository[1] == 'binfiles':
        student_repo = StudentRepoBin(student_file[1])
        discipline_repo = DisciplineRepoBin(discipline_file[1])
        grade_repo = GradeRepoBin(discipline_repo, student_repo, grade_file[1])
    elif repository[1] == 'txtfiles':
        student_repo = StudentRepoText(student_file[1])
        discipline_repo = DisciplineRepoText(discipline_file[1])
        grade_repo = GradeRepoText(discipline_repo, student_repo, grade_file[1])
    else:
        raise ValueError('Invalid settings')

    student_valid = StudentValidator()
    discipline_valid = DisciplineValidator()
    grade_valid = GradeValidator()
    undo_service = UndoService()
    student_service = StudentService(student_repo, student_valid, undo_service)
    discipline_service = DisciplineService(discipline_repo, discipline_valid, undo_service)
    grade_service = GradeService(grade_repo, grade_valid, student_repo, discipline_repo, undo_service)
    ui = MenuUI(student_service, discipline_service, grade_service, undo_service)
    return ui


ui = settings()
ui.start()
