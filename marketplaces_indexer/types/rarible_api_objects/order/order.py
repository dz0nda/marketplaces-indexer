from datetime import datetime
from typing import Optional

from humps.main import camelize

from marketplaces_indexer.models import OrderStatusEnum
from marketplaces_indexer.models import PlatformEnum
from marketplaces_indexer.producer.const import KafkaTopic
from marketplaces_indexer.types.rarible_api_objects import AbstractRaribleApiObject
from marketplaces_indexer.types.rarible_api_objects.asset.asset import AbstractAsset
from marketplaces_indexer.types.tezos_objects.asset_value.asset_value import AssetValue
from marketplaces_indexer.types.tezos_objects.asset_value.xtz_value import Xtz
from marketplaces_indexer.types.tezos_objects.tezos_object_hash import ImplicitAccountAddress


class RaribleApiOrder(AbstractRaribleApiObject):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
        use_enum_values = True

    _kafka_topic = KafkaTopic.ORDER_TOPIC
    fill: Xtz
    platform: PlatformEnum
    status: OrderStatusEnum
    started_at: datetime
    ended_at: Optional[datetime]
    make_stock: AssetValue
    cancelled: bool
    created_at: datetime
    last_updated_at: datetime
    make_price: Xtz
    maker: ImplicitAccountAddress
    taker: Optional[ImplicitAccountAddress]
    make: AbstractAsset
    take: Optional[AbstractAsset]
    salt: int
