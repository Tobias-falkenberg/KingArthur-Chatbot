import requests
from bs4 import BeautifulSoup

# Target page
url = "https://shop.kingarthurbaking.com/mixes"

# User-Agent to avoid 406 errors
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

# Download page
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
products = soup.select("li.product")

print("Products Found:", len(products))

all_products = []

for product in products:

    # Find important elements
    article = product.select_one("article")
    rating_div = product.select_one(".kab-product-rating")
    link = product.select_one("a.card-figure__link")
    img = product.select_one("img")

    # Build product dictionary
    product_data = {
        "product_id": article.get("data-entity-id"),
        "name": article.get("data-name"),
        "url": link.get("href"),
        "price": article.get("data-product-price"),

        "rating": rating_div.get("data-rating"),
        "review_count": rating_div.get("data-reviews"),

        "categories": [
            category.strip()
            for category in article.get("data-product-category").split(",")
        ],

        "image_url": img.get("src")
    }

    all_products.append(product_data)

print("\nPRODUCT DATA")
print("Total Products:", len(all_products))
print("-" * 50)
print("all_products : ", all_products)
print("-" * 50)