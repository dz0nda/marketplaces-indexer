from dipdup.context import HandlerContext
from dipdup.models import TokenTransferData

# from marketplaces_indexer.producer.helper import producer_send
from marketplaces_indexer.types.rarible_api_objects.activity.token.factory import RaribleApiTokenActivityFactory


async def on_transfer(
    ctx: HandlerContext,
    token_transfer: TokenTransferData,
) -> None:
    token_transfer_activity = RaribleApiTokenActivityFactory.build(token_transfer, ctx.datasource)
    assert token_transfer_activity
    # await producer_send(token_transfer_activity)
