class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix = sum of nums[0..j-1]
        prefix = 0
        # for each value v, min_prefix[v] = minimum prefix sum P[i] seen so far at positions i with nums[i] == v
        min_prefix = {}
        ans = float('-inf')
        
        for v in nums:
            # Check both possibilities: nums[i] == v + k or v - k
            for target in (v + k, v - k):
                if target in min_prefix:
                    # sum(nums[i..j]) = (prefix + v) - min_prefix[target]
                    ans = max(ans, prefix + v - min_prefix[target])
            
            # Now record/update prefix sum at this position for future j's
            if v in min_prefix:
                min_prefix[v] = min(min_prefix[v], prefix)
            else:
                min_prefix[v] = prefix
            
            # Add current value to prefix sum
            prefix += v
        
        # If we never found any good subarray, return 0
        return ans if ans != float('-inf') else 0
