#!/usr/bin/env python3
"""
Task 2's module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Fifo class"""

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Add an item to cache"""
        if item is None or key is None:
            pass
        else:
            isInCache = self.cache_data.get(key)
            cache_keys = list(self.cache_data.keys())
            cond = isInCache is None
            if len(cache_keys) >= BaseCaching.MAX_ITEMS and cond:
                self.cache_data.__delitem__(cache_keys[-1])
                self.cache_data.update({key: item})
                print("DISCARD: {}".format(cache_keys[-1]))
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        """Get an item from cache"""
        if self.cache_data.get(key) is not None:
            return self.cache_data.get(key)
        return None
