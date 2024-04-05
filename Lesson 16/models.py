from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc

# Task 6
class Base(DeclarativeBase):
    pass

# def __repr__(self) -> str:
#     return f"Users(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, age={self.age!r})"


class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]


engine = create_engine("sqlite://", echo=False)
Base.metadata.create_all(engine)


with Session(engine) as session:
    Woo = User(
        first_name="Jhon",
        last_name="Woo",
        age=74
    )
    Spilberg = User(
        first_name="Steven",
        last_name="Spilberg",
        age=75
    )
    Liman = User(
        first_name="Doug",
        last_name="Liman",
        age=57
    )
    Marshal = User(
        first_name="Garry",
        last_name="Marshal",
        age=82
    )
    Scorsese = User(
        first_name="Martin",
        last_name="Scorsese",
        age=80
    )

# Task 7
    session.add_all([Woo, Spilberg, Liman, Marshal, Scorsese])
    session.commit()
    # stmt = select(User)
# Task 8
#   stmt = select(User).order_by(desc(User.age)).limit(3)
# Task 9
    stmt = select(User).where(User.first_name == 'Jhon')
    for user in session.scalars(stmt):
        print(f"id={user.id}, first_name={user.first_name}, last_name={user.last_name}, age={user.age})")
