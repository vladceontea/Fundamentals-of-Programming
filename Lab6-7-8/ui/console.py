

class MenuUI:
    def __init__(self, student_service, discipline_service, grade_service, undo_service):
        self._commands = {'1': self.add_student, '2': self.remove_student, '3': self.update_student, '4': self.show_students, '5': self.add_discipline, '6': self.remove_discipline, '7': self.update_discipline, '8': self.show_disciplines, '9': self.add_grades, '10': self.search, '11': self.statistics, '12': self.undo, '13': self.redo, 'secret': self.show_grades}
        self._student_service = student_service
        self._discipline_service = discipline_service
        self._grade_service = grade_service
        self._undo_service = undo_service

    def add_student(self):
        student_id = int(input("ID of new student: "))
        name = input("Name of new student: ")
        self._student_service.add_student(student_id, name)

    def remove_student(self):
        student_id = int(input("ID of the student to be removed: "))
        self._grade_service.delete_grades_student(student_id)
        self._student_service.delete_student(student_id)

    def update_student(self):
        student_id = int(input("ID of the student to be updated: "))
        name = input("New name of the student: ")
        self._student_service.update_student(student_id, name)

    def show_students(self):
        for student in self._student_service.student_repo.student_list:
            print(str(student))

    def add_discipline(self):
        discipline_id = int(input("ID of new discipline: "))
        name = input("Name of new discipline: ")
        self._discipline_service.add_discipline(discipline_id, name)

    def remove_discipline(self):
        discipline_id = int(input("ID of the discipline to be removed: "))
        self._grade_service.delete_grades_discipline(discipline_id)
        self._discipline_service.delete_discipline(discipline_id)

    def update_discipline(self):
        discipline_id = int(input("ID of the discipline to be updated: "))
        name = input("New name of the discipline: ")
        self._discipline_service.update_discipline(discipline_id, name)

    def show_disciplines(self):
        for discipline in self._discipline_service.discipline_repo.discipline_list:
            print(str(discipline))

    def add_grades(self):
        new_list = []
        student_id = int(input("ID of student which receives the grade: "))
        discipline_id = int(input("ID of the discipline at which the grade is received: "))
        done = False
        answer = 'Yes'
        while done is False:
            if answer == 'Yes':
                grade_value = int(input("The numerical value of the grade: "))
                grade = self._grade_service.create_grade(student_id, discipline_id, grade_value)
                new_list.append(grade)
            answer = input("Do you want to add another grade?")
            if answer == 'No':
                self._grade_service.add_grades(new_list)
                done = True
            elif answer != 'Yes' and answer != 'No':
                print("Not a valid answer")

    def show_grades(self):
        for grade in self._grade_service.grade_repo.grade_list:
            print(str(grade))

    def search(self):
        string = input("Enter text here: ")
        k = 0
        for discipline in self._discipline_service.discipline_repo.discipline_list:
            if string.lower() in discipline.name.lower() or string in str(discipline.discipline_id):
                print(str(discipline))
                k = k + 1
        for student in self._student_service.student_repo.student_list:
            if string.lower() in student.name.lower() or string in str(student.student_id):
                print(str(student))
                k = k + 1
        if k == 0:
            print("No matches for your search")

    def statistics(self):
        print("    1. List all students failing at one or more disciplines")
        print("    2. List the students with the best school situation, sorted in descending order of their aggregated average")
        print("    3. List all the disciplines at which there is at least one grade, sorted in descending order of the average grade received by all students enrolled at that discipline")
        number = int(input("Enter which statistic you wish to see (1,2,3): "))
        if number == 1:
            fail_list = self._grade_service.student_fail()
            for student in fail_list:
                print(str(student))
        elif number == 2:
            top_list, average_list = self._grade_service.top_students()
            i = 0
            for student in top_list:
                print(str(student) + '\033[36m' + ' School situation: ' + '\033[0m' + str(average_list[i]))
                i = i + 1
        elif number == 3:
            top_list, average_list = self._grade_service.top_disciplines()
            i = 0
            for discipline in top_list:
                print(str(discipline) + '\033[31m' + ' School situation: ' + '\033[0m' + str(average_list[i]))
                i = i + 1
        else:
            print("This statistic doesn't exist")

    def undo(self):
        if self._undo_service.index == -1:
            print("No undo can be done")
        else:
            self._undo_service.undo()

    def redo(self):
        if self._undo_service.index == len(self._undo_service.history) - 1:
            print("No redo can be done")
        else:
            self._undo_service.redo()

    @staticmethod
    def _print_menu():
        print('0. Exit')
        print('1. Add a student       5. Add a discipline')
        print('2. Remove a student    6. Remove a discipline')
        print('3. Update a student    7. Update a discipline')
        print('4. List all students   8. List all disciplines')
        print('9. Add grades          10. Search disciplines/students')
        print('11. Show statistics')
        print('12. Undo               13. Redo')

    def start(self):
        self.test_init_students()
        self.test_init_disciplines()
        self.test_init_grades()
        while True:
            self._print_menu()
            _command = input("Enter command: ")
            try:
                if _command == '0':
                    print('Exited application')
                    return
                if _command not in self._commands:
                    print('Invalid command!')
                else:
                    self._commands[_command]()
            except Exception as ex:
                print(ex)

    def test_init_students(self):
        for i in range(10):
            self._student_service._student_repo.add_random_student()

    def test_init_disciplines(self):
        for i in range(10):
            self._discipline_service._discipline_repo.add_random_discipline()

    def test_init_grades(self):
        for i in range(10):
            self._grade_service._grade_repo.add_random_grade()
