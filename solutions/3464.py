class Solution(object):
    def maximumTotalCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # running alternating prefix sum
        pa = 0
        
        # best over j even: max(DP[j-1] - PA[j-1])
        best_even = 0  
        # best over j odd : max(DP[j-1] + PA[j-1])
        best_odd  = -10**30  
        
        dp_i = 0
        for i, x in enumerate(nums):
            # update PA[i]
            if i & 1:
                pa -= x
            else:
                pa += x
            
            # compute DP[i]
            dp_i = max(best_even + pa,
                       best_odd  - pa)
            
            # now fold in j = i+1 as a potential start for future segments
            if (i+1) & 1:  # j odd
                best_odd = max(best_odd, dp_i + pa)
            else:          # j even
                best_even = max(best_even, dp_i - pa)
        
        return dp_i
