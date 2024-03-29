
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.reflection import Inspector


class AlembicHelper:
    """A helper class for Alembic migrations."""

    def __init__(self, conn: Connection) -> None:
        self.conn = conn


    def table_exists(self, table: str) -> bool:
        """Method for checking if a table exists."""
        inspector = Inspector.from_engine(self.conn)
        tables = inspector.get_table_names()

        if table not in tables:
            return False

        return True
