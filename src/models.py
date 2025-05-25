from pydantic import BaseModel

class HoraireModel(BaseModel):
    jour: str
    horaires_ouverture: str
    horaires_fermeture: str

class TarifModel(BaseModel):
    nom: str
    pour: str
    montant: float
    devise: str
    categorie: str

class LieuModel(BaseModel):
    tarifs: list[TarifModel]
    horaires: list[HoraireModel]
    jours_fermeture: list[str]
    dates_feries: list[str]
