import pytest
from app.schemas import MusiqueCreate
from pydantic import ValidationError

def test_valid_immatriculation():
    m = MusiqueCreate(titre="T",artiste="Jean Dupont",immatriculation="JD/120/POP/0001")
    assert m.immatriculation

@pytest.mark.parametrize("code", ["XX/059/POP/0001","JD/120/XXX/0001","JD/120/POP/6012"])
def test_invalid_immatriculation(code):
    with pytest.raises(ValidationError):
        MusiqueCreate(titre="T",artiste="Jean Dupont",immatriculation=code)