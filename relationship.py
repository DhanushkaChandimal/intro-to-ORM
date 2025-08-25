from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# Database connection
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/mydatabase', echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass

# User model
class User(Base):
    __tablename__ = "user_account"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(200))

    # One-to-Many: User -> List of Pet objects
    pets: Mapped[List["Pet"]] = relationship(back_populates="owner", cascade="all, delete-orphan")

# Pet model
class Pet(Base):
    __tablename__ = "pets"

    # Columns
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    # Many-to-One: Pet -> User
    owner: Mapped["User"] = relationship(back_populates="pets")

# Create tables
Base.metadata.create_all(engine)
