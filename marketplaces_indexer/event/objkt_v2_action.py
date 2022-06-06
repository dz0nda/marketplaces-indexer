from dipdup.datasources.tzkt.datasource import TzktDatasource
from dipdup.models import Transaction

from marketplaces_indexer.event.abstract_action import AbstractOrderCancelEvent
from marketplaces_indexer.event.abstract_action import AbstractOrderListEvent
from marketplaces_indexer.event.abstract_action import AbstractOrderMatchEvent
from marketplaces_indexer.event.dto import CancelDto
from marketplaces_indexer.event.dto import ListDto
from marketplaces_indexer.event.dto import MakeDto
from marketplaces_indexer.event.dto import MatchDto
from marketplaces_indexer.event.dto import TakeDto
from marketplaces_indexer.models import PlatformEnum
from marketplaces_indexer.types.objkt_marketplace_v2.parameter.ask import AskParameter
from marketplaces_indexer.types.objkt_marketplace_v2.parameter.fulfill_ask import FulfillAskParameter
from marketplaces_indexer.types.objkt_marketplace_v2.parameter.retract_ask import RetractAskParameter
from marketplaces_indexer.types.objkt_marketplace_v2.storage import ObjktMarketplaceV2Storage
from marketplaces_indexer.types.rarible_api_objects.asset.enum import AssetClassEnum
from marketplaces_indexer.types.tezos_objects.asset_value.asset_value import AssetValue
from marketplaces_indexer.types.tezos_objects.asset_value.xtz_value import Xtz
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import ImplicitAccountAddress
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import OriginatedAccountAddress


class ObjktV2OrderListEvent(AbstractOrderListEvent):
    platform = PlatformEnum.OBJKT_V2
    ObjktListTransaction = Transaction[AskParameter, ObjktMarketplaceV2Storage]

    @staticmethod
    def _get_list_dto(
        transaction: ObjktListTransaction,
        datasource: TzktDatasource,
    ) -> ListDto:
        make_value = AssetValue(transaction.parameter.editions)
        make_price = Xtz.from_u_tezos(transaction.parameter.amount)

        return ListDto(
            internal_order_id=str(int(transaction.storage.next_ask_id) - 1),
            maker=ImplicitAccountAddress(transaction.data.sender_address),
            make_price=make_price,
            make=MakeDto(
                asset_class=AssetClassEnum.MULTI_TOKEN,
                contract=OriginatedAccountAddress(transaction.parameter.token.address),
                token_id=int(transaction.parameter.token.token_id),
                value=make_value,
            ),
            take=TakeDto(
                asset_class=AssetClassEnum.XTZ,
                contract=None,
                token_id=None,
                value=Xtz(make_value * make_price),
            ),
        )


class ObjktV2OrderCancelEvent(AbstractOrderCancelEvent):
    platform = PlatformEnum.OBJKT_V2
    ObjktCancelTransaction = Transaction[RetractAskParameter, ObjktMarketplaceV2Storage]

    @staticmethod
    def _get_cancel_dto(transaction: ObjktCancelTransaction, datasource: TzktDatasource) -> CancelDto:
        return CancelDto(internal_order_id=transaction.parameter.__root__)


class ObjktV2OrderMatchEvent(AbstractOrderMatchEvent):
    platform = PlatformEnum.OBJKT_V2
    ObjktMatchTransaction = Transaction[FulfillAskParameter, ObjktMarketplaceV2Storage]

    @staticmethod
    def _get_match_dto(transaction: ObjktMatchTransaction, datasource: TzktDatasource) -> MatchDto:
        return MatchDto(
            internal_order_id=transaction.parameter.ask_id,
            match_amount=AssetValue(1),
            match_timestamp=transaction.data.timestamp,
        )
