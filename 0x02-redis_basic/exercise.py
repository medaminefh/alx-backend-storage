#!/usr/bin/env python3

"""
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.
"""


import redis
import uuid
from typing import Callable


def count_calls(method: Callable):
    def wrapper(*args, **kwargs):
        key = args[0]
        cache = Cache()
        value = cache.get_int(key)
        if value is None:
            value = method(*args, **kwargs)
            cache.store(value)
        else:
            print(f"Cache hit for {key}")
        return value
    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Cache class.

        This method initializes the Cache class by creating an instance of the Redis client and flushing the instance's database.

        Parameters:
            None

        Returns:
            None
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Store the given data in Redis using a randomly generated UUID as the key.

        Parameters:
            data (Any): The data to be stored in Redis.

        Returns:
            str: The generated UUID key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key):
        """
        Get the value associated with the given key from the Redis cache.

        Parameters:
            key (str): The key to retrieve the value for.

        Returns:
            bytes or None: The value associated with the key, or None if the key does not exist.
        """
        return self._redis.get(key)

    def get_str(self, key):
        """
        Get the value associated with the given key from the Redis cache.

        Parameters:
            key (str): The key to retrieve the value for.

        Returns:
            str or None: The value associated with the key, or None if the key does not exist.
        """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key):
        """
        Get the value associated with the given key from the Redis cache.

        Parameters:
            key (str): The key to retrieve the value for.

        Returns:
            int or None: The value associated with the key, or None if the key does not exist.
        """
        return int(self._redis.get(key))
