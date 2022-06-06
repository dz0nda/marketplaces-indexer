from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.rarible_action import RaribleOrderListEvent
from marketplaces_indexer.types.rarible_exchange.parameter.sell import SellParameter
from marketplaces_indexer.types.rarible_exchange.storage import RaribleExchangeStorage


async def rarible_order_list(
    ctx: HandlerContext,
    sell: Transaction[SellParameter, RaribleExchangeStorage],
) -> None:
    await RaribleOrderListEvent.handle(sell, ctx.datasource)
