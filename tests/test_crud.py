import pytest
from app.database import SessionLocal, engine
from app.models import Base, Musique, Magasin, Genre
from app.crud import create_musique, get_all_musiques, create_magasin, add_musique_to_magasin

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_crud_musique(db):
    m = create_musique(db, type('X',(),{'titre':'A','artiste':'Jean Dupont','immatriculation':'JD/130/RAP/0002'}) )
    assert m.id
    allm = get_all_musiques(db)
    assert len(allm) == 1

def test_crud_magasin(db):
    s = create_magasin(db, type('Y',(),{'type_genre':Genre.RAP}))
    s2 = add_musique_to_magasin(db, s.id, 1)
    assert len(s2.musiques)==1