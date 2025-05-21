from collections import Counter, defaultdict

class Solution:
    def findMatrix(self, nums):
        freq = Counter(nums)
        max_rows = max(freq.values())
        result = [[] for _ in range(max_rows)]

        position = defaultdict(int)
        for num in nums:
            row = position[num]
            result[row].append(num)
            position[num] += 1

        return result
