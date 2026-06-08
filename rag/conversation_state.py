class ConversationState:

    def __init__(self):

        self.chat_history = []

        self.last_product = None

        self.awaiting_scope_choice = False

        self.pending_question = None

    def set_last_product(
        self,
        product
    ):
        self.last_product = product

    def get_last_product(
        self
    ):
        return self.last_product

    def set_current_products(
        self,
        products
    ):
        self.current_products = products

    def get_current_products(
        self
    ):
        return self.current_products

    def add_message(
        self,
        role,
        message
    ):
        self.chat_history.append(
            f"{role}: {message}"
        )

        self.chat_history = (
            self.chat_history[-6:]
        )

    def get_history_text(
        self
    ):
        return "\n".join(
            self.chat_history
        )
        
    def set_awaiting_scope(
        self,
        value
    ):
        self.awaiting_scope_choice = value
        
    def is_awaiting_scope(
        self
    ):
        return self.awaiting_scope_choice
    
    def set_pending_question(
        self,
        question
    ):
        self.pending_question = question
        
    def get_pending_question(
        self
    ):
        return self.pending_question