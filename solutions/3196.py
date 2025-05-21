class Solution(object):
    def maxFrequencyScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        # prefix sums: S[i] = sum(nums[0..i])
        S = [0] * n
        S[0] = nums[0]
        for i in range(1, n):
            S[i] = S[i-1] + nums[i]
        
        def range_sum(i, j):
            """Sum of nums[i..j], inclusive."""
            return S[j] - (S[i-1] if i > 0 else 0)
        
        l = 0
        ans = 1
        for r in range(n):
            # Expand window to [l..r], then shrink l until cost <= k
            while l < r:
                m = (l + r) // 2
                # cost to make all in [l..r] equal to nums[m]
                left_cnt = m - l + 1
                left_sum = range_sum(l, m)
                left_cost = nums[m] * left_cnt - left_sum
                
                right_cnt = r - m
                right_sum = range_sum(m+1, r) if m+1 <= r else 0
                right_cost = right_sum - nums[m] * right_cnt
                
                if left_cost + right_cost <= k:
                    break
                l += 1
            
            # update answer
            curr_len = r - l + 1
            if curr_len > ans:
                ans = curr_len
        
        return ans
