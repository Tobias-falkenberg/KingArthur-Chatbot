def needs_clarification(
    question,
    current_products
):
    """
    Decide whether the question is ambiguous.
    """

    if not current_products:
        return False

    question = question.lower()

    ambiguous_phrases = [

        "most expensive",
        "cheapest",
        "highest rated",
        "lowest rated",
        "most reviewed",
    ]

    return any(
        phrase in question
        for phrase in ambiguous_phrases
    )


def build_clarification_message():

    return (
        "\nDo you mean:\n\n"
        "1. filtered  -> among current products\n"
        "2. global    -> entire catalog\n\n"
        "Please type:\n"
        "filtered\n"
        "or\n"
        "global"
    )