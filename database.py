from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./addressbook.db", echo=True)


Base = declarative_base()

# create Session class from sessionmaker for convenient entry
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
