from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.hen_action import HENOrderListEvent
from marketplaces_indexer.types.hen_marketplace.parameter.swap import SwapParameter
from marketplaces_indexer.types.hen_marketplace.storage import HenMarketplaceStorage


async def hen_order_list(
    ctx: HandlerContext,
    swap: Transaction[SwapParameter, HenMarketplaceStorage],
) -> None:
    await HENOrderListEvent.handle(swap, ctx.datasource)
