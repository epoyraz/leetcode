class Solution:
    def maxProfit(self, inventory, orders):
        MOD = 10**9 + 7

        # 1) Sort descending and append a 0 at the end as sentinel
        inventory.sort(reverse=True)
        inventory.append(0)

        ans = 0
        n = len(inventory)
        k = 1  # number of colors at the current top height

        for i in range(n - 1):
            H = inventory[i]
            H2 = inventory[i+1]
            if H > H2:
                # We have k piles at height H, next distinct height is H2
                cnt = k * (H - H2)  # total balls if we fully deplete down to H2
                if orders >= cnt:
                    # Sell the whole block from H down to H2+1
                    # Sum of an arithmetic sequence: (first+last)*#terms//2
                    block_value = k * (H + H2 + 1) * (H - H2) // 2
                    ans = (ans + block_value) % MOD
                    orders -= cnt
                else:
                    # We can't take the whole block: partial
                    d = orders // k  # full levels we can remove
                    r = orders % k   # leftover single sales
                    # Value from full d levels: k * (2H - d + 1) * d // 2
                    full_levels_val = k * (2*H - d + 1) * d // 2
                    # Plus r sales at height H-d
                    remainder_val = r * (H - d)
                    ans = (ans + full_levels_val + remainder_val) % MOD
                    return ans

            # Move to next height
            k += 1

        return ans
