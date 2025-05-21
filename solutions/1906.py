class Solution(object):
    def maxScore(self, nums):
        n = len(nums)
        memo = {}

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            if mask in memo:
                return memo[mask]

            max_score = 0
            turn = bin(mask).count('1') // 2 + 1

            for i in range(n):
                if not (mask & (1 << i)):
                    for j in range(i + 1, n):
                        if not (mask & (1 << j)):
                            new_mask = mask | (1 << i) | (1 << j)
                            score = turn * gcd(nums[i], nums[j]) + dp(new_mask)
                            max_score = max(max_score, score)

            memo[mask] = max_score
            return max_score

        return dp(0)
