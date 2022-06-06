from marketplaces_indexer.producer.container import ProducerContainer
from marketplaces_indexer.types.rarible_api_objects import AbstractRaribleApiObject


async def producer_send(api_object: AbstractRaribleApiObject):
    producer = ProducerContainer.get_instance()
    await producer.send(topic=api_object.kafka_topic, key=api_object.id, value=api_object)
