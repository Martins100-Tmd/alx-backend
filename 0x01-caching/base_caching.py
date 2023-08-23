#!/usr/bin/env python3
"""
BaseCaching module
"""


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initialize"""
        self.cache_data = {}

    def print_cache(self):
        """
        print the cache
        """
        print("Current Cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item to the cache"""
        raise NotImplementedError("Put must be implemented in your cache")

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError("Get must be implemented in your cache")

