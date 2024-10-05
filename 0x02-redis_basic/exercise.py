#!/usr/bin/env python3
""" Imported Redis and uuid"""

import redis
from uuid import uuid4
from typing import Union
from functools import wraps


def count_calls(func):
    """function decorator

    Args:
        func (function): the function to be wraped

    Returns:
        object: callable function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """function wrapper

        Returns:
            wrapper: the function wrapper
        """
        redis_instance = args[0]
        redis_instance._redis.incr(func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


class Cache:
    def __init__(self) -> None:
        """Initialize a cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]):
        """stores an data to the redis cache

        Args:
            data (str | bytes | int | float): the data to be stored
        """
        key = str(uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key, fn=None):
        """Convert the redis data retrieved to the desired format

        Args:
            key (str): the key to be retrieved
            fn (function, optional): the function to convert the retrieved value to the desired format. Defaults to None.
        """
        data = self._redis.get(key)
        if not data:
            return None
        if fn:
            data = fn(data)
            return data
        return data

    def get_str(self, key):
        """Automatically parametrize get with the correct conversion function"""
        return self.get(key=key, fn=str)

    def get_int(self, key):
        """Automatically parametrize get with the correct conversion function"""
        return self.get(key=key, fn=int)
