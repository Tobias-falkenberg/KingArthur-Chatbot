import requests
from bs4 import BeautifulSoup

url = "https://shop.kingarthurbaking.com/mixes"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.select("li.product")

print(products[0].prettify)
