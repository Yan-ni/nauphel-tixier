from crawl4ai import CrawlerRunConfig
import strategies

crawler_config = CrawlerRunConfig(
    extraction_strategy=strategies.llm_strategy,
    exclude_all_images=True,
    excluded_tags=["style", "script", "head"],
    only_text=True
)