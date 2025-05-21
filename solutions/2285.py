class Bitset:
    def __init__(self, size):
        self.n = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx):
        actual = self.bits[idx] ^ self.flipped
        if actual == 0:
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx):
        actual = self.bits[idx] ^ self.flipped
        if actual == 1:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self):
        self.flipped = not self.flipped
        self.ones = self.n - self.ones

    def all(self):
        return self.ones == self.n

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        return ''.join(str(self.bits[i] ^ self.flipped) for i in range(self.n))
