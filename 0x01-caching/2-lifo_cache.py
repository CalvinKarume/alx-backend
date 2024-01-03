#!/usr/bin/python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Additem in the cache """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.queue[-1]]
                print(f"DISCARD: {self.queue[-1]}")
                self.queue.pop(-1)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Getitem by key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
