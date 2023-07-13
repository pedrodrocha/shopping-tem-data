from abc import ABC, abstractmethod
from json import load

from models import Base


class Seeder(ABC):
    @property
    @abstractmethod
    def session(self) -> None:
        """
        A sqlalchemy session instance.
        """
        pass

    @abstractmethod
    def run(self) -> None:
        """
        Method for running a seeder.
        """
        pass

    def import_json(self, json_path: str) -> list:
        """
        Method for importing a json file for seeding the database.
        """
        with open(json_path, encoding="utf-8") as file:
            return load(file)

    def check_exists(self, model: Base, **kwargs: dict) -> bool:
        """
        Method for checking if entry exists in database
        """
        query = self.session.query(model).filter_by(**kwargs)
        return self.session.query(query.exists()).scalar()







