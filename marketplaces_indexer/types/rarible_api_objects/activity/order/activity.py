import uuid
from datetime import datetime
from typing import Literal
from typing import Optional
from typing import Union

from marketplaces_indexer.models import ActivityTypeEnum
from marketplaces_indexer.models import PlatformEnum
from marketplaces_indexer.producer.const import KafkaTopic
from marketplaces_indexer.types.rarible_api_objects import AbstractRaribleApiObject
from marketplaces_indexer.types.rarible_api_objects.asset.asset import AbstractAsset
from marketplaces_indexer.types.tezos_objects.asset_value.xtz_value import Xtz
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import ImplicitAccountAddress
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import OperationHash


class AbstractRaribleApiOrderActivity(AbstractRaribleApiObject):
    _kafka_topic = KafkaTopic.ACTIVITY_TOPIC
    type: str
    order_id: uuid.UUID
    source: PlatformEnum
    hash: OperationHash
    date: datetime
    reverted: bool = False


class RaribleApiOrderListActivity(AbstractRaribleApiOrderActivity):
    type: Literal[ActivityTypeEnum.ORDER_LIST] = ActivityTypeEnum.ORDER_LIST
    maker: ImplicitAccountAddress
    make: AbstractAsset
    take: Optional[AbstractAsset]
    price: Xtz


class RaribleApiOrderMatchActivity(AbstractRaribleApiOrderActivity):
    type: Literal[ActivityTypeEnum.ORDER_MATCH] = ActivityTypeEnum.ORDER_MATCH
    nft: AbstractAsset
    payment: Optional[AbstractAsset]
    buyer: ImplicitAccountAddress
    seller: ImplicitAccountAddress
    price: Xtz


class RaribleApiOrderCancelActivity(AbstractRaribleApiOrderActivity):
    type: Literal[ActivityTypeEnum.ORDER_CANCEL] = ActivityTypeEnum.ORDER_CANCEL
    maker: ImplicitAccountAddress
    make: AbstractAsset
    take: Optional[AbstractAsset]


RaribleApiOrderActivity = Union[RaribleApiOrderListActivity, RaribleApiOrderMatchActivity, RaribleApiOrderCancelActivity]
