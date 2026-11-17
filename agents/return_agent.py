from schemas.schemas import ReturnRequest
from tools.return_tool import create_return


state = ReturnRequest()

def process_message(user_input):
    global state

    text = user_input.lower()

    # Capture order id
    if "order" in text:
        words = text.split()

        for word in words:
            if word.isdigit():
                state.order_id = word

    # Capture item
    if "headphone" in text:
        state.item = "headphones"

    # Capture reason
    if "damaged" in text:
        state.reason = "damaged"

    # Ask for missing fields
    if not state.order_id:
        return "What is your order number?"

    if not state.item:
        return "What item would you like to return?"

    if not state.reason:
        return "What is the reason for return?"

    result = create_return(
        state.order_id,
        state.item,
        state.reason
    )

    return result