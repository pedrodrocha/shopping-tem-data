
from sqlalchemy import select

import models
from seeders.seeder import Seeder
from shopping_data import Session


class CitySeeder(Seeder):
    def __init__(self, session: Session, import_path: str) -> None:
        self.session = session
        self.import_path = import_path
        self.data = self.import_json(self.import_path)

    def session(self) -> None:
        return self.session

    def run(self) -> None:
        for city in self.data:
            exists = self.check_exists(models.City, code=city["city_code"])
            if exists is False:
                self.add_city(city)


    def add_city(self, city: dict) -> None:
        """
        Method for adding a new city to the database.
        """
        state = self.get_state(city["state_code"])

        new_city = models.City(
            code=city["city_code"],
            city=city["city"],
            state=state,
        )
        self.session.add(new_city)
        self.session.commit()

    def get_state(self, state_code: int) -> models.State:
        """
        Method for getting the state a city belongs to.
        """
        return self.session.execute(
            select(models.State).where(models.State.code == state_code),
        ).scalars().first()


