from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
)

from .meta import Base


class User(Base):
    """The user object."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    firstname = Column(Unicode)
    lastname = Column(Unicode)
    email = Column(Unicode)
    username = Column(Unicode)
    password = Column(Unicode)
    food = Column(Unicode)
