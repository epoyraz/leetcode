class CustomStack(object):
    def __init__(self, maxSize):
        self.stack = []
        self.inc = [0] * maxSize
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        if i > 0:
            self.inc[i - 1] += self.inc[i]
        res = self.stack.pop() + self.inc[i]
        self.inc[i] = 0
        return res

    def increment(self, k, val):
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val
