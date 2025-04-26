from .database import SessionLocal, engine
from .models import Base, Musique, Genre, Magasin

Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    # Créer magasins pour chaque genre
    for g in Genre:
        db.add(Magasin(type_genre=g))
    db.commit()
    # Ajouter musiques samples
    samples = [
        {"titre":"Song A","artiste":"Jean Honoré","immatriculation":"JH/180/POP/0001"},
        {"titre":"Track B","artiste":"Paul Durant","immatriculation":"PD/200/RAP/0002"},
        {"titre":"Beat C","artiste":"Renaud Neris","immatriculation":"RN/240/RNB/0003"},
    ]
    for s in samples:
        m = Musique(
            titre=s['titre'], artiste=s['artiste'],
            immatriculation=s['immatriculation'],
            genre=Genre[s['immatriculation'].split('/')[2]],
            duree_sec=int(s['immatriculation'].split('/')[1])
        )
        db.add(m)
    db.commit()
    # Lier musiques aux magasins
    magasins = db.query(Magasin).all()
    musiques = db.query(Musique).all()
    for s in magasins:
        for m in musiques:
            if m.genre == s.type_genre:
                s.musiques.append(m)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()