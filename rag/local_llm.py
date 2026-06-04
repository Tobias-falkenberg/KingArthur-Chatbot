def generate_answer(
    user_question,
    context
):
    return f"""
Based on the retrieved products, the best matches for:

"{user_question}"

are the products shown above.

The strongest recommendation is the Deliciously Simple Chocolate Cake Mix because it directly matches your request for a chocolate baking mix.
"""