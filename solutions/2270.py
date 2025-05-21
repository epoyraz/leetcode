from collections import Counter

class Solution:
    def findLonely(self, nums):
        freq = Counter(nums)
        res = []
        for num in freq:
            if freq[num] == 1 and freq[num - 1] == 0 and freq[num + 1] == 0:
                res.append(num)
        return res
