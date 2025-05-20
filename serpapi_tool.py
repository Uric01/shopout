import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def get_product_data(product_name: str):
    search = GoogleSearch({
        "q": product_name,
        "engine": "google_shopping",
        "api_key": SERPAPI_KEY
    })

    results = search.get_dict()
    items = results.get("shopping_results", [])
    
    data = []
    for item in items:
        data.append({
            "title": item.get("title"),
            "price": item.get("price"),
            "source": item.get("source"),
            "link": item.get("link")
        })

    df = pd.DataFrame(data)
    return df
