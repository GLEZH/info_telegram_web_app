from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True)
    photo = Column(String)
    full_name = Column(String)
    tg_nickname = Column(String)
    birth_date = Column(Date)
    country = Column(String)
    language = Column(String)
    primary_docs = Column(String)
    secondary_docs = Column(String)

    users = relationship("User", back_populates="linked_person")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    linked_person_id = Column(Integer, ForeignKey('persons.id'))

    linked_person = relationship("Person", back_populates="users")