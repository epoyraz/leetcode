from itertools import combinations

class Solution(object):
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        group = n // k
        # precompute valid subsets of size 'group' and their incompatibility
        subsets = {}
        for comb in combinations(range(n), group):
            seen = set()
            valid = True
            for i in comb:
                if nums[i] in seen:
                    valid = False
                    break
                seen.add(nums[i])
            if not valid:
                continue
            mask = 0
            for i in comb:
                mask |= 1 << i
            vals = [nums[i] for i in comb]
            subsets[mask] = max(vals) - min(vals)

        full = (1 << n) - 1
        dp = {0: 0}
        for mask in range(full + 1):
            if mask not in dp:
                continue
            cnt = bin(mask).count('1')
            if cnt == n:
                continue
            if cnt % group != 0:
                continue
            base = dp[mask]
            for sm, inc in subsets.items():
                if mask & sm == 0:
                    nxt = mask | sm
                    dp[nxt] = min(dp.get(nxt, float('inf')), base + inc)

        return dp.get(full, -1)
