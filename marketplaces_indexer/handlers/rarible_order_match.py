from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.rarible_action import RaribleOrderMatchEvent
from marketplaces_indexer.types.rarible_exchange.parameter.buy import BuyParameter
from marketplaces_indexer.types.rarible_exchange.storage import RaribleExchangeStorage


async def rarible_order_match(
    ctx: HandlerContext,
    buy: Transaction[BuyParameter, RaribleExchangeStorage],
) -> None:
    await RaribleOrderMatchEvent.handle(buy, ctx.datasource)
