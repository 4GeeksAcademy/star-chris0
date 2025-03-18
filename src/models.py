import os
import sys
from sqlalchemy import Column, ForeignKey, Integer,String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active= Column(String(444), default=True, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Character(Base):
    __tablename__="character"
    id=Column(Integer,primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(50), nullable=True)
    skin_color= Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    birth_year = Column(String(50), nullable=True)
    gender = Column(String(20), nullable=True)
    homeworld_id = Column(Integer,ForeignKey("planet.id"), nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld_id": self.homeworld_id,
        }

class Planet(Base):
    __tablename__="planet"
    id = Column(Integer,primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=True)
    population = Column(Integer, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
        }

class Starship(Base):
    __tablename__="starship"
    id = Column(Integer,primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    starship_class = Column(String(50), nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "starship_class": self.starship_class,
        }

class Favorite(Base):
    __tablename__="favorite"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    planet_id = Column(Integer,ForeignKey("planet.id"), nullable=True)
    starship_id = Column(Integer, ForeignKey("starship.id"), nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "starship_id": self.starship_id,
        }
    try:
        result = render_er(Base, 'diagram.png')
        print("Success! Check the diagram.png file")
    except Exception as e:
        print("There was a problem genering the diagram")
        raise e