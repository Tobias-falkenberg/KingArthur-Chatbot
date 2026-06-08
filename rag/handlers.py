from product_service import (
    get_most_expensive_product,
    get_cheapest_product,
    get_highest_rated_product,
    get_lowest_rated_product,
    get_most_reviewed_product,
)

def handle_most_expensive(products):

    product = get_most_expensive_product(
        products
    )

    answer = (
        f"{product['name']} is the most expensive product.\n"
        f"Price: ${product['price']}\n"
        f"Rating: {product['rating']}\n"
        f"Reviews: {product['review_count']}"
    )

    return product, answer

def handle_cheapest(products):

    product = get_cheapest_product(
        products
    )

    answer = (
        f"{product['name']} is the cheapest product.\n"
        f"Price: ${product['price']}\n"
        f"Rating: {product['rating']}\n"
        f"Reviews: {product['review_count']}"
    )

    return product, answer

def handle_highest_rated(products):

    product = get_highest_rated_product(
        products
    )

    answer = (
        f"{product['name']} is the highest rated product.\n"
        f"Price: ${product['price']}\n"
        f"Rating: {product['rating']}\n"
        f"Reviews: {product['review_count']}"
    )

    return product, answer

def handle_lowest_rated(products):

    product = get_lowest_rated_product(
        products
    )

    answer = (
        f"{product['name']} is the lowest rated product.\n"
        f"Price: ${product['price']}\n"
        f"Rating: {product['rating']}\n"
        f"Reviews: {product['review_count']}"
    )

    return product, answer

def handle_most_reviewed(products):

    product = get_most_reviewed_product(
        products
    )

    answer = (
        f"{product['name']} has the most reviews.\n"
        f"Price: ${product['price']}\n"
        f"Rating: {product['rating']}\n"
        f"Reviews: {product['review_count']}"
    )

    return product, answer
