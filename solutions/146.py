class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        """Add a new node right before tail (most recently used)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)  # move to the end (most recently used)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self._add(node)

        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
