
import models
from seeders.seeder import Seeder
from shopping_data import Session


class StateSeeder(Seeder):
    def __init__(self, session: Session, import_path: str) -> None:
        self.session = session
        self.import_path = import_path
        self.data = self.import_json(self.import_path)

    def session(self) -> None:
        return self.session

    def run(self) -> None:
        for state in self.data:
            exists = self.check_exists(models.State, code=state['code'])

            if exists is False:
                self.add_state(state)

    def add_state(self, state: dict) -> None:
        """
        Method for adding a new state to the database.
        """
        new_state = models.State(
            code=state['code'],
            abbr=state['abbr'],
            state=state['state']
        )
        self.session.add(new_state)
        self.session.commit()
