from pydantic import BaseModel
from typing import List

class PurchasedItem(BaseModel):
    id: int
    name: str
    description: str
    isBought: bool

class PurchasedItemsResponse(BaseModel):
    purchasedItems: List[PurchasedItem]