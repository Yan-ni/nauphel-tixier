from input import places_list

from crawl4ai import AsyncWebCrawler
import asyncio
from utils import get_google_search_result, save_to_excel
import json
from config import crawler_config
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def main():
    # extraction du résultat de recherche google
    search_result_links = get_google_search_result(places_list)

    results = []

    # Initialisation du crawler
    async with AsyncWebCrawler() as crawler:
        for place, search_result_link in search_result_links: # Boocler sur chaque site extrait de google
            # Scraper le site web
            result = await crawler.arun(
                config=crawler_config,
                url=search_result_link.encoded_string(),
            )

            # transformer le résultat en objet JSON
            result = json.loads(result.extracted_content)[0]

            if result.get('error'):
                print('skipped for error.')
                continue

            results.append({
                "data": result,
                "place": place
            })

    save_to_excel(results)


if __name__ == '__main__':
    asyncio.run(main())