import os
import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = os.getenv("DATABASE_URL")

Engine = sqlalchemy.create_engine(DATABASE_URL)

Session = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = sqlalchemy.orm.declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=Engine)
