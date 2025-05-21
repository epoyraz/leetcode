class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        best = float('inf')
        
        for i in range(n):
            cur_or = 0
            # any single element subarray of length 1 suffices when k == 0
            # but the loop will catch that anyway
            for j in range(i, n):
                cur_or |= nums[j]
                if cur_or >= k:
                    # we found a valid subarray [i..j]
                    best = min(best, j - i + 1)
                    break  # no need to extend further from this i
        
        return best if best != float('inf') else -1
