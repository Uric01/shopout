import os
import pandas as pd
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_KEY")  # Make sure your .env uses this exact key name

def get_product_data(product_name: str) -> pd.DataFrame:
    if not product_name.strip():
        return pd.DataFrame(columns=[
            "title", "normal_price", "promotion_price", "source", "product_link", "sponsored"
        ])

    def search_google_shopping(query: str) -> dict:
        params = {
            "engine": "google_shopping",
            "q": query,
            "api_key": SERPAPI_API_KEY,
            "gl": "za",  # Target South Africa region
        }
        return GoogleSearch(params).get_dict()

    # Run searches
    base = search_google_shopping(product_name)
    hifi = search_google_shopping(f"site:hificorp.co.za {product_name}")
    incredible = search_google_shopping(f"site:incredible.co.za {product_name}")

    all_items = []

    def extract_items(raw_items: list, sponsored_flag: bool):
        results = []
        for item in raw_items:
            title = item.get("title", "N/A")
            source = item.get("source", "N/A")
            current_price = item.get("price")
            old_price = item.get("old_price")
            link = item.get("product_link") or item.get("link")

            if not link or not current_price:
                continue

            if old_price:
                normal_price = old_price
                promotion_price = current_price
            else:
                normal_price = current_price
                promotion_price = None

            results.append({
                "title": title,
                "normal_price": normal_price,
                "promotion_price": promotion_price,
                "source": source,
                "product_link": link,
                "sponsored": sponsored_flag,
            })
        return results

    # Extract product entries from all sections
    all_items.extend(extract_items(base.get("shopping_results", []), sponsored_flag=False))
    all_items.extend(extract_items(base.get("inline_ads", []), sponsored_flag=True))
    all_items.extend(extract_items(base.get("ads", []), sponsored_flag=True))
    all_items.extend(extract_items(hifi.get("shopping_results", []), sponsored_flag=False))
    all_items.extend(extract_items(incredible.get("shopping_results", []), sponsored_flag=False))

    # Remove duplicates based on (title, source)
    seen = set()
    final_items = []
    for item in all_items:
        key = (item["title"], item["source"])
        if key not in seen:
            seen.add(key)
            final_items.append(item)

    return pd.DataFrame(final_items) if final_items else pd.DataFrame(columns=[
        "title", "normal_price", "promotion_price", "source", "product_link", "sponsored"
    ])
