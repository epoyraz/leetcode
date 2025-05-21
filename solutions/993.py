class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}  # diff -> tallest shorter side

        for r in rods:
            curr = dp.copy()
            for diff, height in curr.items():
                dp[diff + r] = max(dp.get(diff + r, 0), height)
                dp[abs(diff - r)] = max(dp.get(abs(diff - r), 0), height + min(r, diff))
        
        return dp[0]
