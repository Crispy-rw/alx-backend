#!/usr/bin/python3
"""BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class
    Args:
        BaseCaching (class): Basic class for this class
    """

    def put(self, key, item):
        """put new value into cache_data dictionary
        Args:
            key ([type]): key of dictionary self.cache_data
            item ([type]): value of key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
