from repository.DisciplineRepo import DisciplineRepo
from repository.StudentRepo import StudentRepo
from repository.GradeRepo import GradeRepo
from entity.discipline import DisciplineValidator
from entity.student import StudentValidator
from entity.grade import GradeValidator
from service.StudentService import StudentService
from service.DisciplineService import DisciplineService
from service.GradeService import GradeService
from service.UndoService import UndoService
from ui.console import MenuUI

student_repo = StudentRepo()
discipline_repo = DisciplineRepo()
grade_repo = GradeRepo(discipline_repo, student_repo)
student_valid = StudentValidator()
discipline_valid = DisciplineValidator()
grade_valid = GradeValidator()
undo_service = UndoService()
student_service = StudentService(student_repo, student_valid, undo_service)
discipline_service = DisciplineService(discipline_repo, discipline_valid, undo_service)
grade_service = GradeService(grade_repo, grade_valid, student_repo, discipline_repo, undo_service)
ui = MenuUI(student_service, discipline_service, grade_service, undo_service)
ui.start()
