from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources, typically in module scope
engine = create_engine(config("DB_CONNECTION"))

# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)
