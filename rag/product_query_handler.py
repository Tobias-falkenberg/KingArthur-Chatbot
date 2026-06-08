from product_service import (
    filter_products,
    get_cheapest_product_from_products,
)


def handle_list_products(
    parsed,
    embeddings_data,
    state
):
    products = filter_products(
        embeddings_data,
        parsed["keyword"]
    )

    state.set_current_products(
        products
    )

    return products

def handle_cheapest_keyword_product(
    parsed,
    embeddings_data,
    state
):
    products = filter_products(
        embeddings_data,
        parsed["keyword"]
    )

    state.set_current_products(
        products
    )

    product = (
        get_cheapest_product_from_products(
            products
        )
    )

    state.set_last_product(
        product
    )

    answer = (
        f"{product['name']} "
        f"is the cheapest "
        f"{parsed['keyword']} product."
    )

    return product, answer