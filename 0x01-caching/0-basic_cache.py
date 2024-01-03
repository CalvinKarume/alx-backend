#!/usr/bin/python3
""" BasicCache DICTIONARY"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching.
    Implements a simple caching system without size limits.
    """

    def put(self, key, item):
        """ Add item to cache.
        If key or item is None, no action is taken.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache.
        Returns value for key or None if key is None or not found.
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

