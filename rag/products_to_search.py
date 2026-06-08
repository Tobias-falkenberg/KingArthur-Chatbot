def get_products_to_search(
    scope,
    current_products,
    embeddings_data
):
    """
    Decide which product collection
    should be used for searching.
    """

    if scope == "global":

        return embeddings_data

    if (
        scope == "filtered"
        and current_products
    ):

        return current_products

    if current_products:

        return current_products

    return embeddings_data