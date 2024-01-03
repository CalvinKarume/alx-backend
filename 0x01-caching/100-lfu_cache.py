#!/usr/bin/python3
""" LFU caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Additem in the cache """
        if key and item:
            key_patch = False
            if key in self.cache_data:
                self.queue.remove(key)
                key_patch = True
            elif len(self.cache_data) >= self.MAX_ITEMS:
                for k, val in self.count.items():
                    minimum = min(self.count.values())
                    i = self.queue.index(k)
                    if val == minimum:
                        del self.cache_data[self.queue[i]]
                        del self.count[self.queue[i]]
                        print(f"DISCARD: {self.queue[i]}")
                        self.queue.pop(i)
                        break
            self.queue.append(key)
            self.cache_data[key] = item
            if key_patch:
                self.count[key] += 1
            else:
                self.count[key] = 0

    def get(self, key):
        """ Get item by key """
        if key and key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
