class Solution:
    def mostFrequentEven(self, nums):
        freq = {}
        for x in nums:
            if x % 2 == 0:
                freq[x] = freq.get(x, 0) + 1
        if not freq:
            return -1
        # pick the even number with highest frequency; ties â smaller number
        return max(freq.keys(), key=lambda x: (freq[x], -x))
