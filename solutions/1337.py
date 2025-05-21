import random

class Node(object):
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * level

class Skiplist(object):
    def __init__(self):
        self.MAX_LEVEL = 16
        self.P = 0.5
        self.head = Node(-1, self.MAX_LEVEL)

    def randomLevel(self):
        level = 1
        while random.random() < self.P and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target):
        curr = self.head
        for i in reversed(range(self.MAX_LEVEL)):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num):
        update = [None] * self.MAX_LEVEL
        curr = self.head
        for i in reversed(range(self.MAX_LEVEL)):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        level = self.randomLevel()
        newNode = Node(num, level)
        for i in range(level):
            newNode.forward[i] = update[i].forward[i]
            update[i].forward[i] = newNode

    def erase(self, num):
        update = [None] * self.MAX_LEVEL
        curr = self.head
        found = False
        for i in reversed(range(self.MAX_LEVEL)):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]
        if curr and curr.val == num:
            found = True
            for i in range(self.MAX_LEVEL):
                if update[i].forward[i] != curr:
                    continue
                update[i].forward[i] = curr.forward[i]
        return found
