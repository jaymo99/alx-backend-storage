#!/usr/bin/env python3
"""
exercise module
"""
from functools import wraps
import redis
from typing import Callable, Union
import uuid

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls in Cache class
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Maintains a counter every time the method is called
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Creates & manages cache on Redis server
    """
    def __init__(self) -> None:
        """Class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores input data in Redis using random string.

        Returns the random key used.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """
        Takes a key argument and returns data.

        An optional callable is used to convert the data
        back to the desired format.
        """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """
        Decodes strings from Redis.
        """
        value = self._redis.get(key)
        return value.decode("UTF-8")

    def get_int(self, key: str) -> str:
        """
        Decodes integers from Redis.
        """
        return self.get(key, int)
