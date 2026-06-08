def get_most_expensive_product(products):
    products = sorted(
        products,
        key=lambda x: float(x["price"]),
        reverse=True
    )

    return products[0]


def get_cheapest_product(products):

    products = sorted(
        products,
        key=lambda x: float(x["price"])
    )

    return products[0]


def get_highest_rated_product(products):

    products = sorted(
        products,
        key=lambda x: float(x["rating"]),
        reverse=True
    )

    return products[0]


def get_lowest_rated_product(products):

    products = sorted(
        products,
        key=lambda x: float(x["rating"])
    )

    return products[0]


def get_most_reviewed_product(products):

    products = sorted(
        products,
        key=lambda x: int(x["review_count"]),
        reverse=True
    )

    return products[0]


def get_cheapest_product_from_products(products):

    products = sorted(
        products,
        key=lambda x: float(x["price"])
    )

    global last_product
    last_product = products[0]
    return products[0]

def filter_products(
products,
keyword,
max_price=None,
min_rating=None
):

    filtered = []

    for product in products:

        text = product["text"].lower()

        if keyword.lower() not in text:
            continue

        if (
            max_price is not None
            and float(product["price"]) > max_price
        ):
            continue

        if (
            min_rating is not None
            and float(product["rating"]) < min_rating
        ):
            continue

        filtered.append(product)

    return filtered


def list_products(products):
    for i, product in enumerate(products, start=1):

        print(
            f"{i}. {product['name']} "
            f"(${product['price']})"
        )

def determine_scope(question):

    question = question.lower()

    if any(
        phrase in question
        for phrase in [
            "database",
            "catalog",
            "whole site",
            "entire site",
            "all products",
            "overall",
            "in this site",
            "everything",
            "in the store",
            "across the site"
        ]
    ):
        return "global"

    if any(
        phrase in question
        for phrase in [
            "among them",
            "among these",
            "from these",
            "from the list"
        ]
    ):
        return "filtered"

    return None

def needs_scope_clarification(
    question,
    current_products
):

    if not current_products:
        return False

    question = question.lower()

    ambiguous_questions = [
        "most expensive",
        "cheapest",
        "highest rated",
        "lowest rated",
        "most reviewed"
    ]

    return any(
        phrase in question
        for phrase in ambiguous_questions
    )