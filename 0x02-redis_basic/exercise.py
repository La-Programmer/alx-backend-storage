#!/usr/bin/env python3
"""WRITE STRINGS TO REDIS"""

import redis
from typing import Union
from typing import Callable
from uuid import uuid4


class Cache:
    """Create a Redis instance"""
    def __init__(self) -> None:
        self._redis: redis.Redis = redis.Redis()
    

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key using uuid"""
        key: str = str(uuid4())
        self._redis.set(name=key, value=data)
        return key
    

    def get(self, key: str, fn=None) -> Union[str, int, bytes, float, None]:
        """Get a value from redis and convert it"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieves a value from Redis as a string"""
        return self.get(key, lambda v: v.decode('utf-8'))
    

    def get_int(self, key: str) -> int:
        """Retrieves a value from Redis as an integer"""
        return self.get(key, int)
