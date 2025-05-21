class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding
        self.i = 0

    def next(self, n):
        while self.i < len(self.encoding):
            if self.encoding[self.i] >= n:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]
            n -= self.encoding[self.i]
            self.i += 2
        return -1
