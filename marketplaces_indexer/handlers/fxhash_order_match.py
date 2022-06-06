from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.types.fxhash_marketplace.parameter.collect import CollectParameter
from marketplaces_indexer.types.fxhash_marketplace.storage import FxhashMarketplaceStorage

async def fxhash_order_match(
    ctx: HandlerContext,
    collect: Transaction[CollectParameter, FxhashMarketplaceStorage],
) -> None:
    ...