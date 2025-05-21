class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # dp[i][t] = max length of a subsequence ending at i with exactly t transitions
        dp = [[0] * (k+1) for _ in range(n)]
        ans = 0
        
        for i in range(n):
            # You can always start a subsequence at i with 0 transitions
            dp[i][0] = 1
            ans = max(ans, 1)
            
            for j in range(i):
                if nums[j] == nums[i]:
                    # extending without using an extra transition
                    for t in range(k+1):
                        if dp[j][t]:
                            cand = dp[j][t] + 1
                            if cand > dp[i][t]:
                                dp[i][t] = cand
                                if cand > ans:
                                    ans = cand
                else:
                    # extending by using one more transition
                    for t in range(1, k+1):
                        if dp[j][t-1]:
                            cand = dp[j][t-1] + 1
                            if cand > dp[i][t]:
                                dp[i][t] = cand
                                if cand > ans:
                                    ans = cand
        
        return ans
