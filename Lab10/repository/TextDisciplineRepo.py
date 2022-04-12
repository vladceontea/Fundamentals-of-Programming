from entity.discipline import Discipline
from repository.DisciplineRepo import DisciplineRepo


class DisciplineRepoText(DisciplineRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def _save(self):
        f = open(self._file_name, 'wt')
        discipline_list = DisciplineRepo.get_all(self)
        try:
            for discipline in discipline_list:
                discipline_str = str(discipline.discipline_id) + ";" + discipline.name + ";"
                f.write(discipline_str)
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
            discipline = Discipline(int(line[0]), line[1])
            super().add_discipline_repo(discipline)

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
