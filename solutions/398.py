import random

class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        indices = [i for i, num in enumerate(self.nums) if num == target]
        return random.choice(indices)
