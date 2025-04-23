from schemas.purchased_items_schema import PurchasedItem, PurchasedItemsResponse
from fastapi import APIRouter
from services.purchased_items_service import PurchasedItemsService

router = APIRouter(prefix="/api/purchased-items")

@router.get("/", response_model=PurchasedItemsResponse)
async def get_purchased_items():
    return await PurchasedItemsService.get_purchased_items()
