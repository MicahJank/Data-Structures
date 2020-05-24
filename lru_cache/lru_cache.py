import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
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
        self.length = 0
        self.entries = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        value = None
        # if i am unable to pull out a key from self.storage that means the node doesnt exist in which case i should return none
        try:
            value = self.storage[key]
        except KeyError:
            print(f"{key} does not exists in the cache")
            return None
        
        # i still need to loop over the entries where my key and value nodes are stored
        # this is because i need to move both of those nodes to the end of the order and i dont know where in the
        # entries those nodes are
        current_node = self.entries.head
        for _ in range(self.entries.length):
            if current_node.value == key:
                next_node = current_node.next
                self.entries.move_to_end(current_node)
                self.entries.move_to_end(next_node)
                value = next_node.value
            current_node = current_node.next

        return value

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
        current_node = self.entries.head
        for _ in range(self.entries.length):
            if current_node.value == key:
                current_node.next.value = value
                print("changing node")
                return
            current_node = current_node.next

        # if the cache is at max capacity we should remove the oldest item from the cache
        if self.length >= self.limit:
            self.storage.pop(self.entries.head.value)
            self.entries.remove_from_head()
            self.entries.remove_from_head()
            self.length -= 1

        
        self.length += 1

        self.entries.add_to_tail(key)
        self.entries.add_to_tail(value)

        self.storage[key] = value
        print(self.storage)