class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums) % p
        if total == 0:
            return 0
        
        n = len(nums)
        best = n + 1
        prefix = 0
        last = {0: 0}
        
        for k, x in enumerate(nums, 1):
            prefix = (prefix + x) % p
            need = (prefix - total) % p
            if need in last:
                best = min(best, k - last[need])
            last[prefix] = k
        
        return best if best < n else -1
