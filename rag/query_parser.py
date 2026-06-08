def parse_query(question):

    question = question.lower()

    result = {
        "keyword": None,
        "intent": None
    }

    product_keywords = [
        "chocolate",
        "bread",
        "cookie",
        "cake",
        "muffin",
        "pancake",
        "brownie",
        "waffle",
        "pizza",
        "bun",
        "scone"
    ]

    for keyword in product_keywords:

        if keyword in question:

            result["keyword"] = keyword
            break

    words = question.split()

    if any(word in words for word in [
        "all",
        "list",
        "show",
        "display"
    ]):
        result["intent"] = "list"

    elif any(
        phrase in question
        for phrase in [
            "cheapest",
            "lowest price",
            "least expensive"
        ]
    ):
        result["intent"] = "cheapest"

    elif any(
        phrase in question
        for phrase in [
            "most expensive",
            "most expensive product",
            "highest price",
            "costliest",
            "priciest"
        ]
    ):
        result["intent"] = "most_expensive"

    elif any(
        phrase in question
        for phrase in [
            "highest rated",
            "top rated",
            "best rated"
        ]
    ):
        result["intent"] = "highest_rated"

    elif any(
        phrase in question
        for phrase in [
            "lowest rated",
            "worst rated",
            "bottom rated"
        ]
    ):
        result["intent"] = "lowest_rated"

    return result