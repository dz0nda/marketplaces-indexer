from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.types.fxhash_marketplace.parameter.cancel_offer import CancelOfferParameter
from marketplaces_indexer.types.fxhash_marketplace.storage import FxhashMarketplaceStorage

async def fxhash_order_cancel_list(
    ctx: HandlerContext,
    cancel_offer: Transaction[CancelOfferParameter, FxhashMarketplaceStorage],
) -> None:
    ...