import random
import math

class Solution:

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self):
        r = self.radius * math.sqrt(random.random())
        theta = random.uniform(0, 2 * math.pi)
        x = self.xc + r * math.cos(theta)
        y = self.yc + r * math.sin(theta)
        return [x, y]
