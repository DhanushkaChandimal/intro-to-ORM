from sqlalchemy import create_engine
from User import User
from Base import Base
from sqlalchemy.orm import Session
from sqlalchemy import select

# Create an engine for SQLite
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/mydatabase')

Base.metadata.create_all(engine)

# Create a new session
session = Session(engine)

# Create a new user
new_user = User(name='Alice', email='alice@example.com')
new_user2 = User(name='DC', email='dc@example.com')

# Add and commit the user to the database
# session.add(new_user)
# session.add(new_user2)
# session.commit()


# Query all users
query = select(User)
users = session.execute(query).scalars().all()

# Print the users
for user in users:
    print(user.name, user.email)



# Query users with a specific email
query = select(User).where(User.name == "Alice")
user = session.execute(query).scalars().first()

print(user.name)  # Outputs: Alice

# Query users whose name starts with 'A'
users = session.query(User).filter(User.name.like('A%')).all()
for user in users:
    print(user.name, user.email)