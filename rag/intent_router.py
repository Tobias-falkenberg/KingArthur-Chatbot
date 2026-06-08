from handlers import (
    handle_most_expensive,
    handle_cheapest,
    handle_highest_rated,
    handle_lowest_rated,
    handle_most_reviewed,
)

INTENT_HANDLERS = {
    "most_expensive": handle_most_expensive,
    "cheapest": handle_cheapest,
    "highest_rated": handle_highest_rated,
    "lowest_rated": handle_lowest_rated,
    "most_reviewed": handle_most_reviewed,
}

def execute_intent(
    intent,
    products
):
    handler = INTENT_HANDLERS.get(
        intent
    )

    if not handler:

        return None, None

    product, answer = handler(
        products
    )

    print(
        f"DEBUG ROUTER -> {product['name']}"
    )

    return product, answer