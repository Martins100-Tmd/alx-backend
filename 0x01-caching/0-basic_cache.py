#!/usr/bin/env python3
"""
Task 0's module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    - Inherits from BaseCaching class
    - Implemented the void functions
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Add an item to cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})

    def get(self, key):
        """Get an item from cache"""
        if self.cache_data.get(key) is not None:
            return self.cache_data.get(key)
        return None
