#!/usr/bin/env python3
"""
exercise module
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Creates & manages cache on Redis server
    """
    def __init__(self) -> None:
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores input data in Redis using random string.

        Returns the random key used.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
