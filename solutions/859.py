class MyCircularDeque(object):
    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.size = k

    def insertFront(self, value):
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.size) % self.size
        self.queue[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        tail = (self.head + self.count) % self.size
        self.queue[tail] = value
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1
        tail = (self.head + self.count - 1) % self.size
        return self.queue[tail]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
