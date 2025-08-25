from sqlalchemy import create_engine
from User import User
from Base import Base
from sqlalchemy.orm import Session

# Create an engine for SQLite
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/mydatabase')

Base.metadata.create_all(engine)

# Create a new session
session = Session(engine)

# Create a new user
new_user = User(name='Alice', email='alice@example.com')

# Add and commit the user to the database
session.add(new_user)
session.commit()