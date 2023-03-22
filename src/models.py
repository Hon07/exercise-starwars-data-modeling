from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Follower(Base):
    __tablename__='follower'
    id-Column(Integer,primary_key-True)
    from_id-Column(Integer,ForeignKey('person.id'))
    from_user=relationship(Person)
    to_id-Column(Integer,ForeignKey('person.id'))
    to_user-relationship(Person)



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False,unique=True)
    password = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref='user')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    favorites = relationship('Favorite', backref='character')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    diameter = Column(String(250))
    climate = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    population = Column(String(250))
    favorites = relationship('Favorite', backref='planet')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
   

engine = create_engine('postgresql://username:password@localhost/database_name')
Base.metadata.create_all(engine)

render_er(Base,'diagram.png')
