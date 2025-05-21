class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class MyLinkedList(object):
    def __init__(self):
        # Dummy head simplifies edge cases
        self.dummy = Node(0)
        self.size = 0

    def get(self, index):
        # If index is invalid, return -1
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        # Move to the index-th node
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        # Insert at index 0
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        # Insert at index size (end)
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        # If index is greater than size, do nothing
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        # Move prev to the node before insertion point
        for _ in range(index):
            prev = prev.next
        # Insert new node
        node = Node(val, prev.next)
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        # If index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        # Move prev to the node before the one to delete
        for _ in range(index):
            prev = prev.next
        # Remove the node
        prev.next = prev.next.next
        self.size -= 1
