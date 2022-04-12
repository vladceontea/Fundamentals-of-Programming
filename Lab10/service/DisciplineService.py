from entity.discipline import Discipline
from service.UndoService import FunctionCall, Operation


class DisciplineService:

    def __init__(self, discipline_repo, discipline_validator, undo_service):
        self._discipline_repo = discipline_repo
        self._discipline_validator = discipline_validator
        self._undo_service = undo_service

    @property
    def discipline_repo(self):
        return self._discipline_repo

    def add_discipline(self, discipline_id, name):
        """
        Adds a new discipline, checking if it has valid values
        :param discipline_id: The ID of the new discipline
        :param name: The name of the new discipline
        :return: -
        """
        discipline = Discipline(discipline_id, name)
        self._discipline_validator.validate(discipline)
        self._discipline_repo.add_discipline_repo(discipline)

        undo_function = FunctionCall(self._discipline_repo.delete_discipline_repo, discipline_id)
        redo_function = FunctionCall(self._discipline_repo.add_discipline_repo, discipline)

        self._undo_service.record(Operation(undo_function, redo_function))

    def add_random_discipline(self):
        """
        Adds a new discipline with randomized parameters
        :return:
        """
        self._discipline_repo.add_random_discipline()

    def delete_discipline(self, discipline_id):
        """
        Removes a discipline
        :param discipline_id: The ID of hte removed discipline
        :return: -
        """
        self._discipline_repo.delete_discipline_repo(discipline_id)

    def update_discipline(self, discipline_id, name):
        """
        Updates the name of a discipline
        :param discipline_id: The ID of the updated discipline
        :param name: The new name of the discipline
        :return: -
        """
        old_name = ''
        for discipline in self._discipline_repo.discipline_list:
            if discipline.discipline_id == discipline_id:
                old_name = discipline.name

        discipline = Discipline(discipline_id, name)
        self._discipline_validator.validate(discipline)
        self._discipline_repo.update_discipline_repo(discipline_id, name)

        undo_function = FunctionCall(self._discipline_repo.update_discipline_repo, discipline_id, old_name)
        redo_function = FunctionCall(self._discipline_repo.update_discipline_repo, discipline_id, name)

        self._undo_service.record(Operation(undo_function, redo_function))
