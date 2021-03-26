import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Userfav(Base):
    __tablename__ = 'userfav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ('user.id'))
    name = Column(String(30))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(Integer, nullable=False)
    password = Column(String(30))
    user_fav = relationship(Userfav)
    

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    model = Column(Integer)
    passengers = Column(Integer)
    consumables = Column(String(30))
    starship_class = Column(String(30))
    lenght = Column(Integer)
    cargo_capacity = Column(Integer)
    hyperdrive_rating = Column(Integer)
    
class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    height = Column(Integer)
    mass = Column(String(250))
    hair_color = Column(String(30))
    skin_color = Column(String(30))
    eye_color = Column(String(30))
    birth_year = Column(Integer)
    gender = Column(String(30))

class Planets(Base):
    __tablename__ = 'planets' 
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(40))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(30))
    gravity = Column(String(30))
    terrain = Column(String(30))
    population = Column(Integer)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')