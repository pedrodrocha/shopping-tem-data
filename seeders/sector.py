
import models
from seeders.seeder import Seeder
from shopping_data import Session


class SectorSeeder(Seeder):
    def __init__(self, session: Session, import_path: str) -> None:
        self.session = session
        self.import_path = import_path
        self.data = self.import_json(self.import_path)

    def session(self) -> None:
        return self.session

    def run(self) -> None:
        for sector in self.data:
            exists = self.check_exists(models.Sector, sector=sector["sector"])
            if exists is False:
                self.add_sector(sector=sector["sector"])

    def add_sector(self, sector: str) -> None:
        """
        Method for adding a new sector to the database.
        """
        new_sector = models.Sector(
            sector=sector,
        )
        self.session.add(new_sector)
        self.session.commit()
