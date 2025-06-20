from input import places_list

from crawl4ai import AsyncWebCrawler
import asyncio
from utils import get_google_search_result, save_to_excel
import json
from config import crawler_config

async def main():
    # extraction du résultat de recherche google
    search_result_links = get_google_search_result(places_list[:5])

    results = []
    max_retries = 3
    retry_delay = 2  # seconds

    # Initialisation du crawler
    async with AsyncWebCrawler() as crawler:
        for place, search_result_link in search_result_links: # Boucler sur chaque site extrait de google
            for attempt in range(1, max_retries + 1):
                try:
                    # Scraper le site web
                    result = await crawler.arun(
                        config=crawler_config,
                        url=search_result_link.encoded_string(),
                    )
                    # transformer le résultat en objet JSON
                    extracted_content: list = json.loads(result.extracted_content)
                    if len(extracted_content) == 0:
                        raise ValueError("Extraction vide")
                    first_result = extracted_content[0]
                    if first_result.get('error'):
                        raise ValueError(f"Erreur LLM: {first_result.get('error')}")
                    results.append({
                        "data": first_result,
                        "place": place
                    })
                    break  # Succès, sortir de la boucle de retry
                except Exception as e:
                    print(f"[{place}] Erreur lors du scraping ou extraction (tentative {attempt}/{max_retries}): {e}")
                    if attempt < max_retries:
                        await asyncio.sleep(retry_delay)
                    else:
                        print(f"[{place}] Échec après {max_retries} tentatives. Passage au suivant.")

    save_to_excel(results)


if __name__ == '__main__':
    asyncio.run(main())