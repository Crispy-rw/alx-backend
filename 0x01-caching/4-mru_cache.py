#!/usr/bin/python3
"""MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class
    Args:
        BaseCaching (class): Basic class for this class
    """
    def __init__(self):
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """put item into cache_data with MRU algorithm
        Args:
            key ([type]): key of dictionary
            item ([type]): item to insert in dictionary
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get value of cache_data dictionary
        Args:
            key ([type]): key to search into cache_data
        """
        if not key or key not in self.cache_data:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data[key]
