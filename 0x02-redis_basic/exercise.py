#!/usr/bin/env python3
"""WRITE STRINGS TO REDIS"""

import redis
from typing import Union
from typing import Callable
from functools import wraps
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key: str = method.__qualname__
        if self._redis.exists(key):
            self._redis.incr(key)
        else:
            self._redis.set(name=key, value=1)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store list of inputs and outputs to a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        inputs_key: str = f'{method.__qualname__}:inputs'
        outputs_key: str = f'{method.__qualname__}:outputs'
        self._redis.rpush(inputs_key, str(args))
        outputs = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, outputs)
        return outputs
    return wrapper


class Cache:
    """Create a Redis instance"""
    def __init__(self) -> None:
        self._redis: redis.Redis = redis.Redis()

    @count_calls
    @call_history
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
