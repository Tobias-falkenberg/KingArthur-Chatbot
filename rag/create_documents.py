import json


# Load enriched products

with open(
    "data/raw/enriched_products.json",
    "r",
    encoding="utf-8"
) as f:
    products = json.load(f)

print(f"Products Loaded: {len(products)}")


documents = []

for product in products:

    categories_text = ", ".join(
        product.get("categories", [])
    )

    text = f"""
Product Name: {product.get("name", "")}

Price: ${product.get("price", "")}

Categories:
{categories_text}

Rating:
{product.get("rating", "")} stars from {product.get("review_count", "")} reviews

Description:
{product.get("description", "")}
"""

    if product.get("ingredients"):
        text += f"""

    Ingredients:
    {product["ingredients"]}
    """

    if product.get("contains"):
        text += f"""

    Contains:
    {product["contains"]}
""" 

    document = {
        "id": product["product_id"],
        "name": product.get("name"),
        "price": product.get("price"),
        "rating": product.get("rating"),
        "review_count": product.get("review_count"),
        "text": text.strip()
    }

    documents.append(document) 
    
    
with open(
"data/processed/documents.json",
"w",
encoding="utf-8"
) as f:

    json.dump(
        documents,
        f,
        indent=4,
        ensure_ascii=False
    )