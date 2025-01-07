#!/usr/bin/env python3
""" Imported Redis and uuid"""

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def replay(method: Callable):
    """
    Display the history of calls of a particular function.

    Args:
        method (Callable): The method to display the history for.
    """
    # Construct keys for inputs and outputs lists
    key_inputs = f"{method.__qualname__}:inputs"
    key_outputs = f"{method.__qualname__}:outputs"

    # Retrieve lists of inputs and outputs from Redis
    inputs = self._redis.lrange(key_inputs, 0, -1)
    outputs = self._redis.lrange(key_outputs, 0, -1)

    # Print the function name and number of calls
    print(f"{method.__qualname__} was called {len(inputs)} times:")

    # Iterate over inputs and outputs using zip
    for input_data, output_data in zip(inputs, outputs):
        # Convert input_data and output_data from bytes to string
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        # Print each call's details
        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


def count_calls(method: Callable):
    """function decorator

    Args:
        func (function): the function to be wraped

    Returns:
        object: callable function
    """

    @wraps(method)
    def wrapper(self, *args):
        """function wrapper

        Returns:
            wrapper: the function wrapper
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return wrapper


def call_history(method: Callable):
    """function decorator

    Args:
        func (function): the function to be wraped

    Returns:
        object: callable function
    """

    @wraps(method)
    def wrapper(self, *args):
        """function wrapper

        Returns:
            wrapper: the function wrapper
        """
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        self._redis.rpush(f"{method.__qualname__}:outputs", str(method(self, *args)))
        return method(self, *args)

    return wrapper


class Cache:
    def __init__(self) -> None:
        """Initialize a cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
