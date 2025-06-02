from crawl4ai import LLMConfig, LLMExtractionStrategy
import models
from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if MISTRAL_API_KEY is None:
    print("Error: You need to include mistral API Key in the .env file in order to run the script.")
    exit(1)


llm_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="mistral/mistral-small-latest", api_token=MISTRAL_API_KEY
    ),
    schema=models.LieuModel.model_json_schema(),
    extraction_type="schema",
    instruction="À partir du contenu, extraire et Renvoyez un objet JSON unique avec le schema suivant : "
    '{"tarifs": [{"nom": "plein","pour": "","montant": 8.0,"devise": "EUR","categorie": "réduit"}],"horaires": [{"jour": "lundi","horaires_ouverture": "09:00","horaires_fermeture": "18:00"}],"jours_fermeture": [""],"dates_feries": [""]} '
    "Les tarifs sont la liste de tous les tarifs disponibles sur le site. "
    "Les noms des tarifs comme : plein, spécial, gratuit ..etc. "
    "Les categories des tarifs comme : Enfant, etudiant, senior, groupes ..etc. "
    "Le pour peut etre par exemple: Billets d'entré, Visites & activités ...etc. "
    "Veillez à ce que le résultat soit un objet JSON unique.",
)