# src/app/database.py

import json
import logging
import os
from redis import Redis
from redis.exceptions import ConnectionError
from .models import Tire

logger = logging.getLogger(__name__)

redis_client = Redis(
    host=os.environ.get("REDIS_SERVER", "localhost"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    password=os.environ.get("REDIS_PASSWORD", ""),
    decode_responses=True
)
class DBInterface:
    """
    Class responsible to interface with the DB
    """

    def __init__(self, client: Redis = redis_client):
        try:
            self._client = client
            self._client.ping()
        except ConnectionError as e:
            logger.error(f"Failed to connect to Redis: {e}")
            raise e

    def get_tire(self, tire_id: str) -> Tire:
        tire_data = self._client.get(f"tire:{tire_id}")
        if tire_data:
            return Tire.from_dict(json.loads(tire_data))
        return None

    def set_tire(self, tire: Tire) -> bool:
        return self._client.set(f"tire:{tire.id}", json.dumps(tire.to_dict()))

    def delete_tire(self, tire_id: str) -> bool:
        return self._client.delete(f"tire:{tire_id}") > 0

    def get_all_tires(self) -> list[Tire]:
        keys = self._client.keys("tire:*")
        tires = []
        for key in keys:
            tire_data = self._client.get(key)
            if tire_data:
                tires.append(Tire.from_dict(json.loads(tire_data)))
        return tires