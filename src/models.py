import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_ergit 

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    fav_characters= relationship('Fav_characters', backref='user', lazy=True)
    fav_species = relationship('Fav_species', backref='user', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_diameter = Column(String)
    planet_gravity = Column(String)
    planet_population = Column(String)
    planet_climate = Column(String)
    planet_terrain = Column(String)
    planet_created = Column(String)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)
    character_height = Column(String)
    character_mass = Column(String)
    character_gender = Column(String)
    character_created = Column(String)
    character_homeworld = Column(String)
    character_url = Column(String)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    species_name = Column(String)
    species_clasification = Column(String)
    species_designation = Column(String)
    species_homeworld = Column(String)
    species_language = Column(String)
    species_people = Column(String)
    species_crated = Column(String)

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))

class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))

class Fav_species(Base):
    __tablename__ = 'fav_species'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    species_id = Column(Integer, ForeignKey('species.id'))

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
