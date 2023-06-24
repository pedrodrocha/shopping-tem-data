
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.reflection import Inspector

class AlembicHelper:
    """A helper class for alembic migrations"""
    def __init__(self, conn: Connection):
        self.conn = conn 
        pass

    def table_exists(self, table: str) -> bool:
        """Method for checking if a table exists"""

        inspector = Inspector.from_engine(self.conn)
        tables = inspector.get_table_names()
        
        if table not in tables:    
            return False
        
        return True
