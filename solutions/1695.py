class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(nums)
        
        # 1) Build frequency array via difference array
        freq = [0] * (n + 1)
        for l, r in requests:
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        
        # 2) Prefix sum to get frequencies for each index
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq.pop()  # drop the extra
        
        # 3) Sort nums and freq
        nums.sort()
        freq.sort()
        
        # 4) Greedily match largest num with largest freq
        total = 0
        for a, f in zip(nums, freq):
            if f > 0:
                total = (total + a * f) % mod
        
        return total
