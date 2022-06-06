from dipdup.context import HandlerContext
from dipdup.models import Transaction

from marketplaces_indexer.event.objkt_action import ObjktOrderListEvent
from marketplaces_indexer.types.objkt_marketplace.parameter.ask import AskParameter
from marketplaces_indexer.types.objkt_marketplace.storage import ObjktMarketplaceStorage


async def objkt_order_list(
    ctx: HandlerContext,
    ask: Transaction[AskParameter, ObjktMarketplaceStorage],
) -> None:
    await ObjktOrderListEvent.handle(ask, ctx.datasource)
