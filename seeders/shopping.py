from sqlalchemy import select

import models
from seeders.seeder import Seeder
from shopping_data import Session


class ShoppingSeeder(Seeder):
    def __init__(self, session: Session, import_path: str) -> None:
        self.session = session
        self.import_path = import_path
        self.data = self.import_json(self.import_path)

    def session(self) -> None:
        return self.session

    def run(self) -> None:
        for shopping in self.data:
            exists = self.check_exists(
                models.Shopping,
                name=shopping["name"],
                site_url=shopping["site_url"],
            )
            if exists is False:
                self.add_shopping(shopping)

    def add_shopping(self, shopping: dict) -> models.Shopping:
        """
        Method for adding a new shopping to the database.
        """
        shopping_obj = models.Shopping(
            name= shopping["name"],
            site_url=shopping["site_url"],
        )

        shopping_obj = self.add_shopping_address(
            shopping_obj,
            shopping["address"],
        )

        shopping_obj = self.add_shopping_phones(
                shopping_obj,
                shopping["phones"],
        )

        shopping_obj = self.add_shopping_opening_hours(
            shopping_obj,
            shopping["opening_hours"],
        )

        self.session.add(shopping_obj)
        self.session.commit()

        return shopping_obj

    def add_shopping_address(
            self,
            shopping: models.Shopping,
            shopping_address: dict,
    ) -> models.Shopping:
        """
        Method for adding a new shopping address belonging to a shopping.
        """
        new_address = models.ShoppingAddress(
            address_line_1= shopping_address["address_line_1"],
            address_line_2= shopping_address["address_line_2"],
            state= self.get_state(shopping_address["state_code"]),
            city= self.get_city(shopping_address["city_code"]),
            postal_code= shopping_address["postal_code"],
        )

        shopping.shopping_address = new_address

        return shopping

    def add_shopping_phones(
            self,
            shopping: models.Shopping,
            shopping_phones: list,
    ) -> models.Shopping:
        """
        Method for adding new shopping phones belonging to a shopping.
        """
        for phone in shopping_phones:
            new_phone = models.ShoppingPhone(
                phone=phone,
            )
            shopping.shopping_phones.append(new_phone)

        return shopping

    def add_shopping_opening_hours(
            self,
            shopping: models.Shopping,
            shopping_opening_hours: dict,
    ) -> models.Shopping:
        """
        Method for adding new opening hours belonging to a shopping.
        """
        for weekday, hours in shopping_opening_hours.items():
            new_hour = models.ShoppingOpeningHour(
                week_day=weekday,
                opening_hour= hours["opening_hour"],
                closing_hour= hours["closing_hour"],
                shopping=shopping,
            )
            shopping.shopping_opening_hours.append(new_hour)

        return shopping

    def get_state(self, state_code: int) -> models.State:
        """
        Method for getting the state a shopping_address belongs to.
        """
        return self.session.execute(
            select(models.State).where(models.State.code == state_code),
        ).scalars().first()

    def get_city(self, city_code: int) -> models.City:
        """
        Method for getting the city a shopping_address belongs to.
        """
        return self.session.execute(
            select(models.City).where(models.City.code == city_code),
        ).scalars().first()
