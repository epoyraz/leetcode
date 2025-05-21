class Solution(object):
    def countSubMultisets(self, nums, l, r):
        MOD = 10**9 + 7
        from collections import Counter

        # Count zeros separately
        freq = Counter(nums)
        z = freq.pop(0, 0)

        total_sum = sum(val * cnt for val, cnt in freq.items())
        max_s = min(r, total_sum)

        # dp[s] = number of ways to get sum s using non-zero values
        dp = [0] * (max_s + 1)
        dp[0] = 1

        # Bounded knapsack via sliding-window per residue
        for v, c in freq.items():
            for rem in range(v):
                window = 0
                queue = []
                for s in range(rem, max_s + 1, v):
                    window = (window + dp[s]) % MOD
                    queue.append(dp[s])
                    if len(queue) > c + 1:
                        window = (window - queue.pop(0)) % MOD
                    dp[s] = window

        # Multiply each dp[s] by ways to choose zeros: (z+1)
        mult = z + 1
        ans = 0
        # sum over s in [l..r], but s=0 case uses dp[0]*(z+1)
        for s in range(l, max_s + 1):
            ans = (ans + dp[s] * mult) % MOD

        return ans
