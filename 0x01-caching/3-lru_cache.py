#!/usr/bin/python3
"""
Task 4's module
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRU-Cache Class"""

    def __init__(self):
        """Initialization"""
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
                self.cache_data.__delitem__(cache_keys[0])
                self.cache_data.update({key: item})
                print("DISCARD: {}".format(cache_keys[0]))
            else:
                self.cache_data.update({key: item})

    def get(self, key):
        """Retrives an element from cache"""
        isInCache = self.cache_data.get(key)
        if key is None or isInCache is None:
            return None
        else:
            newEntry = {key: isInCache}
            self.cache_data.__delitem__(key)
            self.cache_data.update(newEntry)
            return isInCache
