import requests

def get_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None