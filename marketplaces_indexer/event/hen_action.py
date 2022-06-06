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
from marketplaces_indexer.types.hen_marketplace.parameter.cancel_swap import CancelSwapParameter
from marketplaces_indexer.types.hen_marketplace.parameter.collect import CollectParameter
from marketplaces_indexer.types.hen_marketplace.parameter.swap import SwapParameter
from marketplaces_indexer.types.hen_marketplace.storage import HenMarketplaceStorage
from marketplaces_indexer.types.rarible_api_objects.asset.enum import AssetClassEnum
from marketplaces_indexer.types.tezos_objects.asset_value.asset_value import AssetValue
from marketplaces_indexer.types.tezos_objects.asset_value.xtz_value import Xtz
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import ImplicitAccountAddress
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import OriginatedAccountAddress


class HENOrderListEvent(AbstractOrderListEvent):
    platform = PlatformEnum.HEN
    HENListTransaction = Transaction[SwapParameter, HenMarketplaceStorage]

    @staticmethod
    def _get_list_dto(
        transaction: HENListTransaction,
        datasource: TzktDatasource,
    ) -> ListDto:
        make_value = AssetValue(transaction.parameter.objkt_amount)
        make_price = Xtz.from_u_tezos(transaction.parameter.xtz_per_objkt)

        return ListDto(
            internal_order_id=str(int(transaction.storage.counter) - 1),
            maker=ImplicitAccountAddress(transaction.data.sender_address),
            make_price=make_price,
            make=MakeDto(
                asset_class=AssetClassEnum.MULTI_TOKEN,
                contract=OriginatedAccountAddress(transaction.storage.objkt),
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


class HENOrderCancelEvent(AbstractOrderCancelEvent):
    platform = PlatformEnum.HEN
    HENCancelTransaction = Transaction[CancelSwapParameter, HenMarketplaceStorage]

    @staticmethod
    def _get_cancel_dto(transaction: HENCancelTransaction, datasource: TzktDatasource) -> CancelDto:
        return CancelDto(
            internal_order_id=transaction.parameter.__root__,
        )


class HENOrderMatchEvent(AbstractOrderMatchEvent):
    platform = PlatformEnum.HEN
    HENMatchTransaction = Transaction[CollectParameter, HenMarketplaceStorage]

    @staticmethod
    def _get_match_dto(transaction: HENMatchTransaction, datasource: TzktDatasource) -> MatchDto:
        return MatchDto(
            internal_order_id=transaction.parameter.__root__,
            match_amount=AssetValue(1),
            match_timestamp=transaction.data.timestamp,
        )
