import os
import urllib.request
from serpapi import GoogleSearch
from dotenv import load_dotenv
import pandas as pd

# Load API key from .env
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")


def is_url_alive(url: str) -> bool:
    """
    Checks if a given URL is reachable via a minimal GET request.
    """
    try:
        resp = urllib.request.urlopen(url, timeout=5)
        return resp.status == 200
    except Exception:
        return False


def get_product_data(product_name: str) -> pd.DataFrame:
    """
    Fetches Google Shopping results for a product, limited to South Africa.
    Returns a DataFrame with title, promotion_price, normal_price, source, product_link, and image_link.
    """
    search = GoogleSearch({
        "q": product_name,
        "engine": "google_shopping",
        "api_key": SERPAPI_KEY,
        "location": "South Africa",
        "gl": "za",
        "hl": "en",
        "google_domain": "google.co.za"
    })

    results = search.get_dict()
    items = results.get("shopping_results", [])

    data = []
    for item in items:
        # Try both link fields
        link = item.get("link") or item.get("product_link")
        if not link or not is_url_alive(link):
            continue

        # Price logic
        current_price = item.get("price")
        old_price = item.get("old_price")
        if old_price:
            promotion_price = current_price
            normal_price = old_price
        else:
            promotion_price = None
            normal_price = current_price


        data.append({
            "title": item.get("title"),
            "promotion_price": promotion_price,
            "normal_price": normal_price,
            "source": item.get("source"),
            "product_link": link
        })

    return pd.DataFrame(data)