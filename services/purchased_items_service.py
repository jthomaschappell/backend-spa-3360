import json
from repositories.purchased_items_repository import PurchasedItemsRepository
from schemas.purchased_items_schema import PurchasedItem, PurchasedItemsResponse

class PurchasedItemsService:
    @staticmethod
    async def get_purchased_items() -> PurchasedItemsResponse:
        return await PurchasedItemsRepository.get_purchased_items()