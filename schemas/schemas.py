from pydantic import BaseModel, Field
from typing import Optional

class ReturnRequest(BaseModel):
    order_id: Optional[str] = Field(
        default=None,
        description="Customer order number"
    )

    item: Optional[str] = Field(
        default=None,
        description="Item customer wants to return"
    )

    reason: Optional[str] = Field(
        default=None,
        description="Reason for return"
    )