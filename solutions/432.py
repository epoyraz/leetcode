class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
        
class AllOne:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}  # key -> node

    def _insert_after(self, node, new_node):
        nxt = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def inc(self, key):
        if key not in self.key_node:
            if self.head.next.count != 1:
                new_node = Node(1)
                self._insert_after(self.head, new_node)
            self.head.next.keys.add(key)
            self.key_node[key] = self.head.next
        else:
            node = self.key_node[key]
            nxt = node.next
            if nxt.count != node.count + 1:
                new_node = Node(node.count + 1)
                self._insert_after(node, new_node)
            else:
                new_node = nxt
            new_node.keys.add(key)
            self.key_node[key] = new_node
            node.keys.remove(key)
            if len(node.keys) == 0:
                self._remove(node)

    def dec(self, key):
        node = self.key_node[key]
        if node.count == 1:
            del self.key_node[key]
            node.keys.remove(key)
            if len(node.keys) == 0:
                self._remove(node)
        else:
            prev = node.prev
            if prev.count != node.count - 1:
                new_node = Node(node.count - 1)
                self._insert_after(prev, new_node)
            else:
                new_node = prev
            new_node.keys.add(key)
            self.key_node[key] = new_node
            node.keys.remove(key)
            if len(node.keys) == 0:
                self._remove(node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()