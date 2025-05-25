import pandas as pd

from tqdm import tqdm
from googlesearch import search as google_search
from datetime import datetime
from pydantic import HttpUrl, ValidationError

def get_google_search_result(places_list: list[str]) -> list[tuple[str, HttpUrl]]:
    search_result_links: list[tuple[str, HttpUrl]] = []
    
    for place in tqdm(places_list):
        while res := next(google_search(f"{place} paris horaires tarifs", lang="fr")):
            try:
                resUrl = HttpUrl(res)
            except ValidationError:
                print('the following url is not valid : ', res)
                continue
            break

        search_result_links.append((place, resUrl))
    
    return search_result_links

def save_to_excel(results: list[dict], output_file=f"output_{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.xlsx"):
    tarifs_data: list[dict] = []
    horaires_data: list[dict] = []
    jours_fermeture_data: list[dict] = []
    dates_feries_data: list[dict] = []

    for result in results:
        data = result["data"]
        place = result["place"]

        if data.get('error'):
            continue

        tarifs_data.extend([{**tarif, "place": place} for tarif in data["tarifs"]])
        horaires_data.extend([{**horaire, "place": place} for horaire in data["horaires"]])
        jours_fermeture_data.extend([{"jour_fermeture": jour_fermeture, "place": place} for jour_fermeture in data["jours_fermeture"]])
        dates_feries_data.extend([{"dates_feries": date_ferie, "place": place} for date_ferie in data["dates_feries"]])

    tarifs_df = pd.DataFrame(tarifs_data, columns=["place", "nom", "pour", "montant", "devise", "categorie"])
    horaires_df = pd.DataFrame(horaires_data, columns=["place", "jour", "horaires_ouverture", "horaires_fermeture"])
    jours_fermeture_df = pd.DataFrame(jours_fermeture_data, columns=["place", "jour_fermeture"])
    dates_feries_df = pd.DataFrame(dates_feries_data, columns=["place", "dates_feries"])

    with pd.ExcelWriter(f"output/{output_file}", engine="openpyxl") as writer:
        tarifs_df.to_excel(writer, sheet_name="Tarifs", index=False)
        horaires_df.to_excel(writer, sheet_name="Horaires", index=False)
        jours_fermeture_df.to_excel(writer, sheet_name="jour_fermeture", index=False)
        dates_feries_df.to_excel(writer, sheet_name="dates_feries", index=False)
