from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.objkt_action import ObjktOrderCancelEvent
from marketplaces_indexer.types.objkt_marketplace.parameter.retract_ask import RetractAskParameter
from marketplaces_indexer.types.objkt_marketplace.storage import ObjktMarketplaceStorage


async def objkt_order_cancel_list(
    ctx: HandlerContext,
    retract_ask: Transaction[RetractAskParameter, ObjktMarketplaceStorage],
) -> None:
    await ObjktOrderCancelEvent.handle(retract_ask, ctx.datasource)
