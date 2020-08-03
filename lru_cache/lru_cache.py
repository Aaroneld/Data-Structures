from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()

    def __str__(self):

        self.cache.__str__()
        return 'Done'

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        
        if self.cache.contains(key):
            node = self.cache.contains(key)
            self.cache.move_to_end(node["node"])
            return node["value"]


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        if self.cache.contains(key):
            node = self.cache.contains(key)
            setattr(node["node"], key, value)
            self.cache.move_to_end(node["node"])      
        elif len(self.cache) >= self.limit:
            self.cache.remove_from_head()
            self.cache.add_to_tail(key, value)
        else:
            self.cache.add_to_tail(key, value)

cache = LRUCache(3)
cache.set("item1", 1)
cache.set("item2", 2)
cache.set("item3", 3)

print(cache)

print(cache.get("item1"))


print(cache)

cache.set("item4", 4)


print(cache)