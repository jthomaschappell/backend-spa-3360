import json
from schemas.purchased_items_schema import PurchasedItem, PurchasedItemsResponse

class PurchasedItemsRepository:
    @staticmethod
    async def get_purchased_items() -> PurchasedItemsResponse:
        with open('db/database.json', 'r') as f:
            data = json.load(f)
            return PurchasedItemsResponse(purchasedItems=data['purchasedItems'])
