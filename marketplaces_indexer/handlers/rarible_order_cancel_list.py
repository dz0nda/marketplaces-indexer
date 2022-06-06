from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.rarible_action import RaribleOrderCancelEvent
from marketplaces_indexer.types.rarible_exchange.parameter.cancel_sale import CancelSaleParameter
from marketplaces_indexer.types.rarible_exchange.storage import RaribleExchangeStorage


async def rarible_order_cancel_list(
    ctx: HandlerContext,
    cancel_sale: Transaction[CancelSaleParameter, RaribleExchangeStorage],
) -> None:
    await RaribleOrderCancelEvent.handle(cancel_sale, ctx.datasource)
