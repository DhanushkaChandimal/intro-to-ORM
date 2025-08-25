from sqlalchemy import String
from Base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "new_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50))