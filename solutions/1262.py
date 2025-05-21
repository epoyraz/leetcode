import random
import bisect
from collections import defaultdict

class MajorityChecker(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        self.indices = defaultdict(list)
        for i, val in enumerate(arr):
            self.indices[val].append(i)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for _ in range(20):  # Try 20 random samples for high probability
            rand_index = random.randint(left, right)
            candidate = self.arr[rand_index]
            idx_list = self.indices[candidate]
            l = bisect.bisect_left(idx_list, left)
            r = bisect.bisect_right(idx_list, right)
            if r - l >= threshold:
                return candidate
        return -1
