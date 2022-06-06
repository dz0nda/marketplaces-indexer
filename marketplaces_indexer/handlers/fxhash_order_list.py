from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.types.fxhash_marketplace.parameter.offer import OfferParameter
from marketplaces_indexer.types.fxhash_marketplace.storage import FxhashMarketplaceStorage

async def fxhash_order_list(
    ctx: HandlerContext,
    offer: Transaction[OfferParameter, FxhashMarketplaceStorage],
) -> None:
    ...