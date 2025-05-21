class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        cover = [0] * (n + 1)
        
        # Build coverage counts via difference array
        for l, r in queries:
            cover[l]   += 1
            cover[r+1] -= 1
        
        # Prefix sum to get how many queries cover each index
        for i in range(1, n):
            cover[i] += cover[i-1]
        
        # Check feasibility: each nums[i] needs that many decrements,
        # but can only decrement at most cover[i] times.
        for i in range(n):
            if cover[i] < nums[i]:
                return False
        
        return True
