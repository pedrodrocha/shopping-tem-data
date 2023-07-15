
from sqlalchemy import select

import models
from seeders.seeder import Seeder
from shopping_data import Session


class SubsectorSeeder(Seeder):
    def __init__(self, session: Session, import_path: str) -> None:
        self.session = session
        self.import_path = import_path
        self.data = self.import_json(self.import_path)

    def session(self) -> None:
        return self.session

    def run(self) -> None:
        for subsector in self.data:
            sector = self.get_sector(subsector["sector"])
            if sector is not None:
                exists = self.check_exists(
                            models.Subsector,
                            sector_id=sector.id,
                            subsector=subsector["subsector"],
                        )
                if exists is False:
                    self.add_subsector(subsector, sector)


    def add_subsector(self, subsector_data: dict, sector: models.Sector) -> None:
        """
        Method for adding a new subsector to the database.
        """
        new_subsector = models.Subsector(
            subsector=subsector_data["subsector"],
            description=subsector_data["description"],
            sector = sector,
        )

        self.session.add(new_subsector)

        self.session.commit()


    def get_sector(self, sector: str) -> models.Sector | None:
        """
        Method for getting the sector a subsector belongs to.
        """
        return self.session.execute(
            select(models.Sector).where(models.Sector.sector == sector),
        ).scalars().first()

