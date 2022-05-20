from dipdup.context import HandlerContext
from dipdup.models import Transaction

from rarible_marketplace_indexer.event.rarible_action import RaribleOrderListEvent
from rarible_marketplace_indexer.types.rarible_bids.parameter.put_bid import PutBidParameter
from rarible_marketplace_indexer.types.rarible_bids.storage import RaribleBidsStorage


async def rarible_put_bid(
    ctx: HandlerContext,
    sell: Transaction[PutBidParameter, RaribleBidsStorage],
) -> None:
    await RaribleOrderListEvent.handle(sell, ctx.datasource)
