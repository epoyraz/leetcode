import random

class Solution:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1
        x = self.map.get(r, r)
        self.map[r] = self.map.get(self.total, self.total)
        return [x // self.n, x % self.n]

    def reset(self):
        self.total = self.m * self.n
        self.map.clear()
