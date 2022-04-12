from entity.student import Student, StudentException
import random


class StudentRepo:
    def __init__(self):
        self.student_list = []

    def get_all(self):
        return self.student_list

    def add_student_repo(self, student):
        """
        Adds a student to the list of students
        :param student: The new student
        :return: -
        """
        for element in self.student_list:
            if element.student_id == student.student_id:
                raise StudentException('The ID already exists')
            if element.name == student.name:
                raise StudentException('The student name already exists')
        self.student_list.append(student)

    def add_random_student(self):
        """
        Adds a student with randomized parameters to the list of all students
        :return: -
        """
        done = False
        while not done:
            student = Student(random.randint(100, 199), random.choice(student_list))
            double = False
            for element in self.student_list:
                if student.student_id == element.student_id or student.name == element.name:
                    double = True
            if double is False:
                self.student_list.append(student)
                done = True

    def update_student_repo(self, student_id, name):
        """
        Updates the name of a student
        :param student_id: The ID of the student
        :param name: The new name of the student
        :return: -
        """
        updated = False
        for student in self.student_list:
            if student.student_id == student_id:
                student.name = name
                updated = True
        if updated is False:
            raise StudentException('This student does not exist')

    def delete_student_repo(self, student_id):
        """
        Removes a student from the list
        :param student_id: The ID of the student
        :return: -
        """
        deleted = False
        for student in self.student_list:
            if student_id == student.student_id:
                self.student_list.remove(student)
                deleted = True
        if deleted is False:
            raise StudentException('This student does not exist')


student_list = ['Claude Floyd', 'Kenneth Fox', 'Erica Moody', 'Christian Conner', 'Misty Mathis', 'Ervin Reeves', 'Donnie Ruiz', 'Roxanne Mason', 'Marc Lyons', 'Dexter Butler', 'Lorraine Gomez', 'Patrick Perkins', 'Nathan Gross', 'Ken Ferguson', 'Pat Mack', 'Shari Greer', 'Evelyn Olson', 'Susan Welch', 'Vicki Fowler', 'Nellie Roberson', 'Hugo Rodriquez', 'Paula Weber', 'Cristina Cortez', 'Anne Mills', 'Gerard Carter', 'Damon Alvarez', 'Stacey Terry', 'Michelle Jones', 'Denise Ryan', 'Stanley Ramsey']
