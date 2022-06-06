from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.objkt_v2_action import ObjktV2OrderMatchEvent
from marketplaces_indexer.types.objkt_marketplace_v2.parameter.fulfill_ask import FulfillAskParameter
from marketplaces_indexer.types.objkt_marketplace_v2.storage import ObjktMarketplaceV2Storage


async def objkt_v2_order_match(
    ctx: HandlerContext,
    fulfill_ask: Transaction[FulfillAskParameter, ObjktMarketplaceV2Storage],
) -> None:
    await ObjktV2OrderMatchEvent.handle(fulfill_ask, ctx.datasource)
