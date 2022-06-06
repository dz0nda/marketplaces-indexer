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
from marketplaces_indexer.types.objkt_marketplace.parameter.ask import AskParameter
from marketplaces_indexer.types.objkt_marketplace.parameter.fulfill_ask import FulfillAskParameter
from marketplaces_indexer.types.objkt_marketplace.parameter.retract_ask import RetractAskParameter
from marketplaces_indexer.types.objkt_marketplace.storage import ObjktMarketplaceStorage
from marketplaces_indexer.types.rarible_api_objects.asset.enum import AssetClassEnum
from marketplaces_indexer.types.tezos_objects.asset_value.asset_value import AssetValue
from marketplaces_indexer.types.tezos_objects.asset_value.xtz_value import Xtz
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import ImplicitAccountAddress
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import OriginatedAccountAddress


class ObjktOrderListEvent(AbstractOrderListEvent):
    platform = PlatformEnum.OBJKT
    ObjktListTransaction = Transaction[AskParameter, ObjktMarketplaceStorage]

    @staticmethod
    def _get_list_dto(
        transaction: ObjktListTransaction,
        datasource: TzktDatasource,
    ) -> ListDto:
        make_value = AssetValue(transaction.parameter.amount)
        make_price = Xtz.from_u_tezos(transaction.parameter.price)

        return ListDto(
            internal_order_id=str(int(transaction.storage.ask_id) - 1),
            maker=ImplicitAccountAddress(transaction.data.sender_address),
            make_price=make_price,
            make=MakeDto(
                asset_class=AssetClassEnum.MULTI_TOKEN,
                contract=OriginatedAccountAddress(transaction.parameter.fa2),
                token_id=int(transaction.parameter.objkt_id),
                value=make_value,
            ),
            take=TakeDto(
                asset_class=AssetClassEnum.XTZ,
                contract=None,
                token_id=None,
                value=Xtz(make_value * make_price),
            ),
        )


class ObjktOrderCancelEvent(AbstractOrderCancelEvent):
    platform = PlatformEnum.OBJKT
    ObjktCancelTransaction = Transaction[RetractAskParameter, ObjktMarketplaceStorage]

    @staticmethod
    def _get_cancel_dto(transaction: ObjktCancelTransaction, datasource: TzktDatasource) -> CancelDto:
        return CancelDto(internal_order_id=transaction.parameter.__root__)


class ObjktOrderMatchEvent(AbstractOrderMatchEvent):
    platform = PlatformEnum.OBJKT
    ObjktMatchTransaction = Transaction[FulfillAskParameter, ObjktMarketplaceStorage]

    @staticmethod
    def _get_match_dto(transaction: ObjktMatchTransaction, datasource: TzktDatasource) -> MatchDto:
        return MatchDto(
            internal_order_id=transaction.parameter.__root__,
            match_amount=AssetValue(1),
            match_timestamp=transaction.data.timestamp,
        )
