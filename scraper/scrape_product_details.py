import json
import requests
from bs4 import BeautifulSoup

# Load products
with open("data/raw/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

print(f"Products Loaded: {len(products)}")

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

for index, product in enumerate(products, start=1):

    print(f"\n[{index}/{len(products)}] {product['name']}")

    response = requests.get(
        product["url"],
        headers=headers
    )

    # with open(
    #     "debug_product.html",
    #     "w",
    #     encoding="utf-8"
    # ) as f:
    #     f.write(response.text)

    # break

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # -------------------------
    # Description
    # -------------------------

    description_div = soup.select_one(
        ".tab-content-left"
    )

    if description_div:
        description = description_div.get_text(
            separator=" ",
            strip=True
        )
    else:
        description = ""

    # -------------------------
    # Ingredients + Contains
    # -------------------------

    ingredients = ""
    contains = ""

    ingredients_div = soup.select_one(
        ".ingredients-html"
    )
    
    if ingredients_div:
        print("Length:", len(ingredients_div.get_text(strip=True)))
    
    print("\nINGREDIENTS DIV:")
    print("ingredients_div : ", ingredients_div)

    if ingredients_div:

        headings = ingredients_div.find_all("h3")

        for heading in headings:

            title = heading.get_text(strip=True)

            p_tag = heading.find_next_sibling("p")

            if not p_tag:
                continue

            text = p_tag.get_text(
                separator=" ",
                strip=True
            )

            print("text : ", text)
                
            if title == "Ingredients":
                ingredients = text

            elif title == "Contains":
                contains = text

    # Save into product dictionary

    product["description"] = description
    product["ingredients"] = ingredients
    product["contains"] = contains

    # -------------------------
    # Nutrition PDF
    # -------------------------

    nutrition_pdf_url = ""

    nutrition_link = soup.select_one(
        ".nutrition-link"
    )

    if nutrition_link:

        pdf_href = nutrition_link.get("href")

        if pdf_href:

            nutrition_pdf_url = (
                "https://shop.kingarthurbaking.com"
                + pdf_href
            )

    product["nutrition_pdf_url"] = nutrition_pdf_url


# Save enriched data

with open(
    "data/raw/enriched_products.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        products,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nDone!")
print("Saved: data/raw/enriched_products.json")