from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.hen_action import HENOrderCancelEvent
from marketplaces_indexer.types.hen_marketplace.parameter.cancel_swap import CancelSwapParameter
from marketplaces_indexer.types.hen_marketplace.storage import HenMarketplaceStorage


async def hen_order_cancel_list(
    ctx: HandlerContext,
    cancel_swap: Transaction[CancelSwapParameter, HenMarketplaceStorage],
) -> None:
    await HENOrderCancelEvent.handle(cancel_swap, ctx.datasource)
