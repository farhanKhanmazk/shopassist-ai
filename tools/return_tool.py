def create_return(order_id: str, item: str, reason: str):
    return {
        "status": "success",
        "message": "Return request created",
        "order_id": order_id,
        "item": item,
        "reason": reason
    }