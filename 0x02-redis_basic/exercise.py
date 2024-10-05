#!/usr/bin/env python3
""" Imported Redis and uuid"""

import redis
from uuid import uuid4


class Cache:
    def __init__(self) -> None:
        """Initialize a cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float):
        """stores an data to the redis cache

        Args:
            data (str | bytes | int | float): the data to be stored
        """
        key = str(uuid4())
        self._redis.set(name=key, value=data)
        return key
