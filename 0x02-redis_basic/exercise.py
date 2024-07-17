#!/usr/bin/env python3
"""WRITE STRINGS TO REDIS"""

import redis
from typing import Union
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
