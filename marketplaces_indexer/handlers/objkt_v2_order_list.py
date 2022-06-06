from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.objkt_v2_action import ObjktV2OrderListEvent
from marketplaces_indexer.types.objkt_marketplace_v2.parameter.ask import AskParameter
from marketplaces_indexer.types.objkt_marketplace_v2.storage import ObjktMarketplaceV2Storage


async def objkt_v2_order_list(
    ctx: HandlerContext,
    ask: Transaction[AskParameter, ObjktMarketplaceV2Storage],
) -> None:
    await ObjktV2OrderListEvent.handle(ask, ctx.datasource)
