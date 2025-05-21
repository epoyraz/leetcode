import heapq

class Solution(object):
    def minimumIncrements(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        # 1) gcd helper
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        m = len(target)
        full_mask = (1 << m) - 1

        # 2) precompute LCM for each non-empty subset of target (bitmask)
        lcm_of = {}
        for mask in range(1, full_mask + 1):
            L = 1
            for j in range(m):
                if (mask >> j) & 1:
                    t = target[j]
                    L = (L // gcd(L, t)) * t
            lcm_of[mask] = L

        # 3) for each subsetâmask, collect up to m cheapest (inc, index) pairs
        candidate_costs = {}
        for mask, L in lcm_of.items():
            costs = []
            for i, v in enumerate(nums):
                rem = v % L
                inc = (L - rem) % L
                costs.append((inc, i))
            # keep the m smallest by inc
            candidate_costs[mask] = heapq.nsmallest(m, costs)

        # 4) generate all setâpartitions of {0,â¦,mâ1} as lists of masks
        partitions = []
        def backtrack(remaining, parts):
            if remaining == 0:
                partitions.append(parts[:])
                return
            lowb = remaining & -remaining
            sub = remaining
            while sub:
                if sub & lowb:
                    parts.append(sub)
                    backtrack(remaining ^ sub, parts)
                    parts.pop()
                sub = (sub - 1) & remaining

        backtrack(full_mask, [])

        # 5) for each partition, do a small DFS to pick distinct numsâindices
        ans = float('inf')
        for parts in partitions:
            k = len(parts)
            best_for_part = [float('inf')]  # use list to capture âby referenceâ

            def dfs(idx, used, total):
                # prune
                if total >= best_for_part[0]:
                    return
                if idx == k:
                    best_for_part[0] = total
                    return
                mask = parts[idx]
                for cost, i in candidate_costs[mask]:
                    if i not in used:
                        dfs(idx + 1, used | {i}, total + cost)

            dfs(0, set(), 0)
            if best_for_part[0] < ans:
                ans = best_for_part[0]

        return ans
