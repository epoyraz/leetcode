from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        count = Counter(nums)
        ans = 1
        # specialâcase x = 1: you can form the longest odd palindrome of 1âs
        c1 = count.get(1, 0)
        if c1 > 0:
            if c1 % 2 == 1:
                ans = max(ans, c1)
            else:
                ans = max(ans, c1 - 1)
        limit = 10**9
        for x in count:
            if x == 1:
                continue
            # build the chain [x, x^2, x^4, ...] until missing or repeats
            v = x
            seen = set()
            chain = []
            while v <= limit and v in count and v not in seen:
                chain.append(v)
                seen.add(v)
                v = v * v
            # try each possible center at chain[m]
            prefix_ok = True
            for m in range(1, len(chain)):
                if count[chain[m-1]] < 2:
                    prefix_ok = False
                if not prefix_ok:
                    break
                # we know chain[m] exists at least once
                ans = max(ans, 2*m + 1)
        return ans
