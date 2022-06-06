from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.objkt_action import ObjktOrderMatchEvent
from marketplaces_indexer.types.objkt_marketplace.parameter.fulfill_ask import FulfillAskParameter
from marketplaces_indexer.types.objkt_marketplace.storage import ObjktMarketplaceStorage


async def objkt_order_match(
    ctx: HandlerContext,
    fulfill_ask: Transaction[FulfillAskParameter, ObjktMarketplaceStorage],
) -> None:
    await ObjktOrderMatchEvent.handle(fulfill_ask, ctx.datasource)
