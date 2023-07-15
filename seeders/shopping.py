
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
                new_shopping = self.add_shopping(shopping)
                new_shopping = self.add_shopping_address(
                    new_shopping,
                    shopping["address"],
                )
                new_shopping = self.add_shopping_phones(
                    new_shopping,
                    shopping["phones"],
                )
                new_shopping = self.add_shopping_opening_hours(
                    new_shopping,
                    shopping["opening_hours"],
                )

    def add_shopping(self, shopping: dict) -> models.Shopping:
        """
        Method for adding a new shopping to the database.
        """
        new_shopping = models.Shopping(
            name= shopping["name"],
            site_url=shopping["site_url"],
        )

        self.session.add(new_shopping)
        self.session.commit()

        return new_shopping

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
            state= shopping_address["state"],
            city= shopping_address["city"],
            postal_code= shopping_address["postal_code"],
            shopping= shopping,
        )

        self.session.add(new_address)
        self.session.commit()

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
            exists = self.check_exists(
                models.ShoppingPhone,
                shopping_id=shopping.id,
                phone=phone,
            )

            if exists is False:
                new_phone = models.ShoppingPhone(
                    phone=phone,
                    shopping=shopping,
                )
                self.session.add(new_phone)
                self.session.commit()

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
            exists = self.check_exists(
                models.ShoppingOpeningHour,
                shopping_id=shopping.id,
                week_day=weekday,
            )
            if exists is False:
                new_hour = models.ShoppingOpeningHour(
                    week_day=weekday,
                    opening_hour= hours["opening_hour"],
                    closing_hour= hours["closing_hour"],
                    shopping=shopping,
                )
                self.session.add(new_hour)
                self.session.commit()

        return shopping
