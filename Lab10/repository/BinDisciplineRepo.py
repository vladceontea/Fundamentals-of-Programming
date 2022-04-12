import pickle
from repository.DisciplineRepo import DisciplineRepo


class DisciplineRepoBin(DisciplineRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wb')
        discipline_list = DisciplineRepo.get_all(self)
        pickle.dump(discipline_list, f)
        f.close()

    def _load(self):
        try:
            f = open(self._file_name, 'rb')
            self._discipline_list = pickle.load(f)
        except EOFError:
            return []

    def add_discipline_repo(self, discipline):
        super().add_discipline_repo(discipline)
        self._save()

    def delete_discipline_repo(self, discipline_id):
        super().delete_discipline_repo(discipline_id)
        self._save()

    def update_discipline_repo(self, discipline_id, name):
        super().update_discipline_repo(discipline_id, name)
        self._save()

    def add_random_discipline(self):
        super().add_random_discipline()
        self._save()
