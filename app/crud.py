from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

# Musique

def create_musique(db: Session, m: schemas.MusiqueCreate):
    db_m = models.Musique(
        titre=m.titre,
        artiste=m.artiste,
        immatriculation=m.immatriculation,
        genre=models.Genre[m.immatriculation.split('/')[2]],
        duree_sec=int(m.immatriculation.split('/')[1])
    )
    db.add(db_m)
    db.commit()
    db.refresh(db_m)
    return db_m

def get_musique(db: Session, musique_id: int):
    m = db.query(models.Musique).get(musique_id)
    if not m:
        raise HTTPException(status_code=404, detail="Musique non trouvée")
    return m

def get_all_musiques(db: Session):
    return db.query(models.Musique).all()

def update_musique(db: Session, musique_id: int, data: dict):
    db_m = get_musique(db, musique_id)
    for key, value in data.items():
        setattr(db_m, key, value)
    db.commit()
    db.refresh(db_m)
    return db_m

def delete_musique(db: Session, musique_id: int):
    db_m = get_musique(db, musique_id)
    db.delete(db_m)
    db.commit()
    return db_m

# Magasin

def create_magasin(db: Session, m: schemas.MagasinCreate):
    db_s = models.Magasin(type_genre=m.type_genre)
    db.add(db_s)
    db.commit()
    db.refresh(db_s)
    return db_s

def get_magasin(db: Session, magasin_id: int):
    s = db.query(models.Magasin).get(magasin_id)
    if not s:
        raise HTTPException(status_code=404, detail="Magasin non trouvé")
    return s

def get_all_magasins(db: Session):
    return db.query(models.Magasin).all()

def add_musique_to_magasin(db: Session, magasin_id: int, musique_id: int):
    s = get_magasin(db, magasin_id)
    m = get_musique(db, musique_id)
    if m.genre != s.type_genre:
        raise HTTPException(status_code=400, detail="Genre incompatible")
    s.musiques.append(m)
    db.commit()
    db.refresh(s)
    return s

def remove_musique_from_magasin(db: Session, magasin_id: int, musique_id: int):
    s = get_magasin(db, magasin_id)
    m = get_musique(db, musique_id)
    s.musiques.remove(m)
    db.commit()
    db.refresh(s)
    return s