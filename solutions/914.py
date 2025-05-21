import random
import bisect

class Solution:
    def __init__(self, rects):
        self.rects = rects
        self.weights = []
        total = 0
        for a, b, x, y in rects:
            area = (x - a + 1) * (y - b + 1)
            total += area
            self.weights.append(total)
        self.total = total

    def pick(self):
        k = random.randint(1, self.total)
        i = bisect.bisect_left(self.weights, k)
        a, b, x, y = self.rects[i]
        rand_x = random.randint(a, x)
        rand_y = random.randint(b, y)
        return [rand_x, rand_y]
