from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class Genre(enum.Enum):
    RAP = "RAP"
    POP = "POP"
    RNB = "RNB"

class Musique(Base):
    __tablename__ = "musiques"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    artiste = Column(String, nullable=False)
    immatriculation = Column(String, unique=True, nullable=False)
    genre = Column(Enum(Genre), nullable=False)
    duree_sec = Column(Integer, nullable=False)

class Magasin(Base):
    __tablename__ = "magasins"
    id = Column(Integer, primary_key=True, index=True)
    type_genre = Column(Enum(Genre), nullable=False)
    # listes via relations many-to-many ou foreign key