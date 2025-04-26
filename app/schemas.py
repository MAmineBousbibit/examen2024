from pydantic import BaseModel, validator
import re
from .models import Genre

class MusiqueCreate(BaseModel):
    titre: str
    artiste: str
    immatriculation: str

    @validator('immatriculation')
    def check_immatriculation(cls, v, values):
        pattern = r"^([A-Z]{2})/(\d{3})/([A-Z]{3})/(\d{4})$"
        m = re.match(pattern, v)
        if not m:
            raise ValueError("Format invalide")
        init, d_str, g, ident = m.groups()
        # initiales de l’artiste
        art = values.get('artiste','')
        initials = ''.join([p[0].upper() for p in art.split()][:2])
        if initials != init:
            raise ValueError("Initiales ne correspondent pas à l’artiste")
        duree = int(d_str)
        if not (60 < duree < 300):
            raise ValueError("Durée invalide")
        if g not in Genre.__members__:
            raise ValueError("Genre invalide")
        if '6' in ident:
            raise ValueError("Identifiant contient un 6")
        return v