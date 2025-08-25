from sqlalchemy import create_engine
from User import User
from Base import Base

# Create an engine for SQLite
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/mydatabase')

Base.metadata.create_all(engine)