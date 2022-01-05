from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
engine = create_engine('postgresql+psycopg2://user:passwd@localhost:5432/dbname')

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()