from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

# Crée les tables
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- Routes Musique -----
@app.post("/musiques/", response_model=schemas.MusiqueRead)
def create_musique(m: schemas.MusiqueCreate, db: Session = Depends(get_db)):
    return crud.create_musique(db, m)

@app.get("/musiques/", response_model=list[schemas.MusiqueRead])
def list_musiques(db: Session = Depends(get_db)):
    return crud.get_all_musiques(db)

@app.get("/musiques/{musique_id}", response_model=schemas.MusiqueRead)
def get_musique(musique_id: int, db: Session = Depends(get_db)):
    return crud.get_musique(db, musique_id)

@app.put("/musiques/{musique_id}", response_model=schemas.MusiqueRead)
def update_musique(musique_id: int, m: schemas.MusiqueCreate, db: Session = Depends(get_db)):
    return crud.update_musique(db, musique_id, m.dict())

@app.delete("/musiques/{musique_id}", response_model=schemas.MusiqueRead)
def delete_musique(musique_id: int, db: Session = Depends(get_db)):
    return crud.delete_musique(db, musique_id)

# ----- Routes Magasin -----
@app.post("/magasins/", response_model=schemas.MagasinRead)
def create_magasin(s: schemas.MagasinCreate, db: Session = Depends(get_db)):
    return crud.create_magasin(db, s)

@app.get("/magasins/", response_model=list[schemas.MagasinRead])
def list_magasins(db: Session = Depends(get_db)):
    return crud.get_all_magasins(db)

@app.get("/magasins/{magasin_id}", response_model=schemas.MagasinRead)
def get_magasin(magasin_id: int, db: Session = Depends(get_db)):
    return crud.get_magasin(db, magasin_id)

@app.post("/magasins/{magasin_id}/musiques/{musique_id}", response_model=schemas.MagasinRead)
def add_musique(magasin_id: int, musique_id: int, db: Session = Depends(get_db)):
    return crud.add_musique_to_magasin(db, magasin_id, musique_id)

@app.delete("/magasins/{magasin_id}/musiques/{musique_id}", response_model=schemas.MagasinRead)
def remove_musique(magasin_id: int, musique_id: int, db: Session = Depends(get_db)):
    return crud.remove_musique_from_magasin(db, magasin_id, musique_id)