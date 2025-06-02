# Scraping dynamique de sites de lieux touristiques

Le but de ce script est de récupérer des informations de certains lieux touristiques à partir d'une liste définie.

Le script suit les étapes d'execution suivantes :

!["étapes d'execution"](docs/assets/flow-scraping.png)

## Développement

### Prérequis

Pour pouvoir lancer le script, il faut:

* [python](https://www.python.org/downloads/) >= 3.13
* [uv project manager](https://docs.astral.sh/uv/guides/install-python/)
* Mistral AI

Pour intégrer mistralAI:
1. Créer un compte sur [Mistral AI](https://auth.mistral.ai/ui/registration).
2. Sélectionner un plan (le plan gratuit suffit).
3. Créer une api key dans [la console](https://console.mistral.ai/api-keys).
4. Copier la clé API et la coller ici dans un fichier nommé `.env`

### installation des dépendances

Installer les dépendances du projet:
```bash
uv sync
```

Installer playright pour la gestion des navigateurs :

```bash
uv run playwright install
```


### Lancer le script

Pour lancer le script :
```bash
uv run src/main.py
```

Le fichier excel généré sera dans le dosser `output`.