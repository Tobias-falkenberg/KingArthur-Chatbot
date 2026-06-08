from llm_service import ask_llm

SIMPLE_FOLLOWUPS = [
    "tell me more",
    "about that",
    "that product",
    "more details",
    "in detail"
]

LLM_FOLLOWUPS = [

    "summarize",
    "why",
    "compare",
    "worth buying",
]


def is_followup_question(question):

    question = question.lower()

    return any(
        phrase in question
        for phrase in (
            SIMPLE_FOLLOWUPS
            + LLM_FOLLOWUPS
            + [
                "its price",
                "its rating",
                "how much does it cost",
                "how many reviews",
            ]
        )
    )


def handle_followup(
    state,
    chain,
    question
):

    product = state.get_last_product()

    if not product:

        return None

    question = question.lower()

    if (
        "price" in question
        or "cost" in question
    ):
        return (
            f"{product['name']} costs "
            f"${product['price']}"
        )

    if "rating" in question:

        return (
            f"{product['name']} has a rating of "
            f"{product['rating']} stars"
        )

    if "review" in question:

        return (
            f"{product['name']} has "
            f"{product['review_count']} reviews"
        )

    if any(
        phrase in question
        for phrase in SIMPLE_FOLLOWUPS
    ):
        return product["text"]

    if any(
        phrase in question
        for phrase in LLM_FOLLOWUPS
    ):
        return ask_llm(
            chain,
            "",
            product["text"],
            question
        )

    return product["text"]