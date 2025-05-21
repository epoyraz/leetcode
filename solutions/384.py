import random

class Solution:
    def __init__(self, nums):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self):
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
