#!/usr/bin/python3
"""FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add item in the cache """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                del self.cache_data[self.queue[0]]
                print(f"DISCARD: {self.queue[0]}")
                self.queue.pop(0)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get item by key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
