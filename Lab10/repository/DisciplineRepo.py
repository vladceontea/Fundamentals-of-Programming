from entity.discipline import Discipline, DisciplineException
import random

from module import IterableObject


class DisciplineRepo:
    def __init__(self):
        self._discipline_list = IterableObject()

    @property
    def discipline_list(self):
        return self._discipline_list

    def get_all(self):
        return self._discipline_list

    def add_discipline_repo(self, discipline):
        """
        Adds a new discipline
        :param discipline: The new discipline
        :return: -
        """
        for element in self._discipline_list:
            if element.discipline_id == discipline.discipline_id:
                raise DisciplineException('The ID already exists')
            if element.name == discipline.name:
                raise DisciplineException('The discipline name already exists')
        self._discipline_list.add(discipline)

    def add_random_discipline(self):
        """
        Adds a discipline with randomized parameters
        :return: -
        """
        done = False
        while not done:
            discipline = Discipline(random.randint(200, 299), random.choice(discipline_list))
            double = False
            for element in self._discipline_list:
                if discipline.discipline_id == element.discipline_id or discipline.name == element.name:
                    double = True
            if double is False:
                self._discipline_list.add(discipline)
                done = True

    def update_discipline_repo(self, discipline_id, name):
        """
        Updates the name of a discipline
        :param discipline_id: The ID of the updates discipline
        :param name: The new name of the discipline
        :return: -
        """
        updated = False
        for discipline in self._discipline_list:
            if discipline.discipline_id == discipline_id:
                discipline.name = name
                updated = True
        if updated is False:
            raise DisciplineException('This discipline does not exist')

    def delete_discipline_repo(self, discipline_id):
        """
        Removes a discipline from the list of all disciplines
        :param discipline_id: The ID of the removed disciplines
        :return: -
        """
        deleted = False
        i = 0
        while i < len(self._discipline_list):
            if discipline_id == self._discipline_list[i].discipline_id:
                self._discipline_list.__delitem__(i)
                deleted = True
            else:
                i = i + 1
        if deleted is False:
            raise DisciplineException('This discipline does not exist')


discipline_list = ['Language Arts', 'Mathematics', 'Science', 'Health', 'Handwriting', 'Physical Education (P.E.)', 'Art', 'Music', 'Dramatics', 'Dance', 'English', 'Social Studies', 'Geography', 'Computer Science', 'Latin', 'Poetry', 'Chemistry', 'Biology', 'French', 'German', 'Spanish', 'Logic']
