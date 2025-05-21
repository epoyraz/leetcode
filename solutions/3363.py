import heapq
from collections import defaultdict

class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = defaultdict(int)       # current count of each ID
        freq_count = defaultdict(int)  # how many IDs have a given count
        max_heap = []                  # max-heap of counts (stored as negatives)
        ans = [0] * n

        for i in range(n):
            x = nums[i]
            delta = freq[i]

            old = count[x]
            new = old + delta

            # remove from old bucket
            if old > 0:
                freq_count[old] -= 1

            # update count[x]
            if new > 0:
                count[x] = new
                freq_count[new] += 1
                heapq.heappush(max_heap, -new)
            else:
                # new == 0 â remove entirely
                count.pop(x, None)

            # lazy-pop from heap until top is valid
            while max_heap and freq_count[-max_heap[0]] == 0:
                heapq.heappop(max_heap)

            # top of heap is current max count
            ans[i] = -max_heap[0] if max_heap else 0

        return ans
