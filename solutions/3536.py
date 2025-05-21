class Solution(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # dp_prev[a] = number of ways to choose arr1[0..i-1] with arr1[i-1] = a
        # For i = 0, arr1[0] can be any a in [0..nums[0]]
        dp_prev = [1] * (nums[0] + 1)
        
        for i in range(1, n):
            prev_max = len(dp_prev) - 1
            cur_max = nums[i]
            # required jump Î = max(nums[i] - nums[i-1], 0)
            delta = max(nums[i] - nums[i-1], 0)
            
            # build prefix sums of dp_prev for O(1) range sums
            prefix = [0] * (prev_max + 2)
            for a in range(prev_max + 1):
                prefix[a+1] = (prefix[a] + dp_prev[a]) % MOD
            
            # compute dp_cur[b] for b in [0..cur_max]
            dp_cur = [0] * (cur_max + 1)
            for b in range(delta, cur_max + 1):
                # we need a <= b - delta
                limit = b - delta
                if limit > prev_max:
                    limit = prev_max
                # sum of dp_prev[0..limit]:
                dp_cur[b] = prefix[limit + 1]
            
            dp_prev = dp_cur
        
        # total ways = sum of dp_prev over all possible arr1[n-1] values
        return sum(dp_prev) % MOD
