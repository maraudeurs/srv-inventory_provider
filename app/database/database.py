import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.config import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(engine):
    from database.instance_model import Instance
    logging.info("Initializing the database.")
    Instance.metadata.create_all(bind=engine)

def purge_db(engine):
    from database.instance_model import Instance
    logging.info("purging database.")
    Instance.metadata.drop_all(bind=engine)