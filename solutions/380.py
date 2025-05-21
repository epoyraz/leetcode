import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.nums = []

    def insert(self, val):
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_index:
            return False
        idx = self.val_to_index[val]
        last_val = self.nums[-1]
        self.nums[idx] = last_val
        self.val_to_index[last_val] = idx
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)
