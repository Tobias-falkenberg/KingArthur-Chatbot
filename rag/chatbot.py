import os
from sympy import product

os.environ["NO_PROXY"] = "localhost,127.0.0.1"
os.environ["no_proxy"] = "localhost,127.0.0.1"

from data_loader import (
    load_embeddings,
    load_faiss_index,
    load_embedding_model,
    load_llm_chain,
)

from product_service import (
    list_products,
    determine_scope,
)

from rag_service import (
    run_rag_pipeline
)

from intent_matcher import detect_intent
from query_parser import parse_query

from products_to_search import (
    get_products_to_search
)

from conversation_state import (
    ConversationState
)

from intent_router import (
    execute_intent
)

from followup_handler import (
    is_followup_question,
    handle_followup,
)

from product_query_handler import (
    handle_list_products,
    handle_cheapest_keyword_product,
)

from clarification_handler import (
    needs_clarification,
    build_clarification_message,
)    

TOP_K = 2
state = ConversationState()

# Load data
embeddings_data = (
    load_embeddings()
)

index = (
    load_faiss_index()
)

model = (
    load_embedding_model()
)

chain = (
    load_llm_chain()
)

scope = None

try:
    
    while True:
        
        user_question = input(
            "\nAsk a question: "
        )
        user_question = user_question.strip()

        if not user_question:

            print(
                "\nPlease enter a question."
            )

            continue

        if user_question.lower() in [
                "quit",
                "exit"
            ]:
                print("Goodbye!")
                break
        
        if state.is_awaiting_scope():

            if user_question.lower() in [
                "filtered",
                "global"
            ]:

                scope = user_question.lower()

                user_question = (
                    state.get_pending_question()
                )

                state.set_awaiting_scope(
                    False
                )

                state.set_pending_question(
                    None
                )

            else:

                print(
                    "\nPlease type:"
                    "\nfiltered"
                    "\nor"
                    "\nglobal"
                )

                continue
                
        parsed = parse_query(user_question)
        
        if scope is None:
            
            scope = determine_scope(
                user_question
            )

        intent = parsed["intent"]

        if intent is None:

            intent, score = detect_intent(user_question)

            if score < 0.60:
                intent = None
            
        if (
            state.get_last_product()
            and is_followup_question(
                user_question
            )
        ):

            answer = handle_followup(
                state,
                chain,
                user_question
            )

            print("\nANSWER:\n")
            print(answer)

            continue
        
        print(parsed)
        
        if (
            parsed["intent"] == "list"
            and parsed["keyword"]
        ):

            products = handle_list_products(
                parsed,
                embeddings_data,
                state
            )

            print("\nPRODUCTS:\n")

            list_products(products)

            continue
        
        if (
            parsed["intent"] == "cheapest"
            and parsed["keyword"]
        ):

            product, answer = (
                handle_cheapest_keyword_product(
                    parsed,
                    embeddings_data,
                    state
                )
            )

            print("\nANSWER:\n")
            print(answer)

            continue

        if (
            not scope
            and needs_clarification(
                user_question,
                state.get_current_products()
            )
        ):

            print(
                build_clarification_message()
            )

            state.set_awaiting_scope(
                True
            )

            state.set_pending_question(
                user_question
            )

            continue

        products_to_search = (
            get_products_to_search(
                scope,
                state.get_current_products(),
                embeddings_data
            )
        )

        product, answer = execute_intent(
            intent,
            products_to_search
        )

        if product:

            state.set_last_product(
                product
            )
            
            print(
                "DEBUG LAST PRODUCT:",
                state.get_last_product()["name"]
            )
            
            print("\nANSWER:\n")
            print(answer)

            continue

        answer = run_rag_pipeline(
            user_question,
            state,
            model,
            index,
            embeddings_data,
            chain,
            TOP_K
        )

        print("\nANSWER:\n")
        print(answer)
        state.add_message(
            "User",
            user_question
        )

        state.add_message(
            "Assistant",
            answer
        )
        
except KeyboardInterrupt:

    print(
        "\n\nChatbot stopped by user."
    )

except Exception as e:

    print(
        f"\nUnexpected error: {e}"
    )