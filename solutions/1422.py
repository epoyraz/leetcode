from collections import Counter
import heapq

class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        keys = sorted(count)

        for num in keys:
            if count[num] > 0:
                freq = count[num]
                for i in range(num, num + k):
                    if count[i] < freq:
                        return False
                    count[i] -= freq

        return True
