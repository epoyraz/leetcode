import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.val_to_indices = defaultdict(set)
        self.nums = []

    def insert(self, val):
        self.val_to_indices[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.val_to_indices[val]) == 1

    def remove(self, val):
        if not self.val_to_indices[val]:
            return False
        remove_idx = self.val_to_indices[val].pop()
        last_val = self.nums[-1]
        self.nums[remove_idx] = last_val
        self.val_to_indices[last_val].add(remove_idx)
        self.val_to_indices[last_val].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self):
        return random.choice(self.nums)
