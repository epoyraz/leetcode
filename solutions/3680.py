class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra

class Solution(object):
    def countComponents(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        dsu = DSU(n)

        # Map small numbers to their index, and isolate large ones
        present = [-1]*(threshold+1)
        for i, v in enumerate(nums):
            if v <= threshold:
                present[v] = i

        # rep[x] = first index we saw whose value divides x
        rep = [-1]*(threshold+1)

        # For each possible divisor d<=threshold that actually appears,
        # union all other nums[i] dividing the same x.
        for d in range(1, threshold+1):
            i = present[d]
            if i < 0:
                continue
            for x in range(d, threshold+1, d):
                j = rep[x]
                if j < 0:
                    rep[x] = i
                else:
                    dsu.union(i, j)

        # Count unique roots over ALL nodes
        roots = set()
        for i in range(n):
            roots.add(dsu.find(i))
        return len(roots)
