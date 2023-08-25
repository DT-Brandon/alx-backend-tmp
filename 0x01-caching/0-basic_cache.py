#!/usr/bin/python3
"""Module creates a basic caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BaseCaching and overwrites functions 'put' and 'get'.
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
            the value for the key.
        """
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return:
                The value in cache_data with key
        """
        return self.cache_data.get(key)
