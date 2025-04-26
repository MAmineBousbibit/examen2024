from app.main import app
from fastapi.testclient import TestClient

def test_api_musique():
    client = TestClient(app)
    resp = client.post("/musiques/", json={"titre":"T","artiste":"Anne Marie","immatriculation":"AM/140/POP/0005"})
    assert resp.status_code == 200
    data = resp.json()
    assert data['titre']=='T'
    get = client.get(f"/musiques/{data['id']}")
    assert get.status_code==200


def test_api_magasin():
    client = TestClient(app)
    resp = client.post("/magasins/", json={"type_genre":"POP"})
    assert resp.status_code==200
    mid = resp.json()['id']
    # Create a musique to get its ID
    musique_resp = client.post("/musiques/", json={"titre":"T","artiste":"Anne Marie","immatriculation":"AM/140/POP/0005"})
    assert musique_resp.status_code == 200
    data = musique_resp.json()
    # ajouter musique existante
    add = client.post(f"/magasins/{mid}/musiques/{data['id']}")
    assert add.status_code in (200,201)