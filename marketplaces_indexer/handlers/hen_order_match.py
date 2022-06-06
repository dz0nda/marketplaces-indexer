from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.hen_action import HENOrderMatchEvent
from marketplaces_indexer.types.hen_marketplace.parameter.collect import CollectParameter
from marketplaces_indexer.types.hen_marketplace.storage import HenMarketplaceStorage


async def hen_order_match(
    ctx: HandlerContext,
    collect: Transaction[CollectParameter, HenMarketplaceStorage],
) -> None:
    await HENOrderMatchEvent.handle(collect, ctx.datasource)
