import urllib.request

def is_url_alive(url: str) -> bool:
    """
    Checks if a given URL is reachable.
    :param url: The URL to check.
    :return: True if the URL is reachable, False otherwise.
    """
    try:
        request = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(request, timeout=5)
        return response.status == 200
    except Exception:
        return False


def save_df_to_csv(df, filename="shop_out_results.csv"):
    df.to_csv(filename, index=False)
    return filename
