from sqlalchemy import create_engine, String, Table, Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column, relationship
from typing import List, Optional

# Database connection
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/mydatabase', echo=True)

# Base class for models
class Base(DeclarativeBase):
    pass

# Association table for User and Pet
user_pet = Table(
    "user_pet",
    Base.metadata,
    Column("user_id", ForeignKey("user_account.id")),
    Column("pet_id", ForeignKey("pets.id")),
)

# User model
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]] = mapped_column(String(200))

    # Many-to-Many: User <-> Pet
    pets: Mapped[List["Pet"]] = relationship(secondary=user_pet, back_populates="owners")

# Pet model
class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))

    # Many-to-Many: Pet <-> User
    owners: Mapped[List["User"]] = relationship(secondary=user_pet, back_populates="pets")

# Create tables
Base.metadata.create_all(engine)