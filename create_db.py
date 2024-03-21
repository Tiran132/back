from database.tables import Base
from database.db import engine


Base.metadata.create_all(engine)
