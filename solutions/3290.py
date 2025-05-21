class Solution(object):
    def countMatchingSubarrays(self, nums, pattern):
        """
        :type nums: List[int]
        :type pattern: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(pattern)
        if m == 0:
            # pattern of length 0: every adjacent pair counts, so n-1 subarrays
            return n - 1
        
        # Build the diff array of length n-1, where
        # diff[i] = sign(nums[i+1] - nums[i]) in {-1,0,1}
        diff = [0] * (n - 1)
        for i in range(n - 1):
            d = nums[i+1] - nums[i]
            if d > 0:
                diff[i] = 1
            elif d < 0:
                diff[i] = -1
            else:
                diff[i] = 0
        
        # KMP prefix-function on the pattern
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
        
        # KMP search for pattern in diff
        count = 0
        j = 0
        for x in diff:
            while j > 0 and x != pattern[j]:
                j = pi[j-1]
            if x == pattern[j]:
                j += 1
                if j == m:
                    count += 1
                    j = pi[j-1]
        
        return count
