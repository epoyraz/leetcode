class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, v):
        # add v at index i (1-based)
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def query(self, i):
        # sum of fw[1..i]
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        A = [nums1[i] - nums2[i] for i in range(n)]
        # Gather all values we will need to rank:
        vals = set(A)
        vals.update(a + diff for a in A)
        # Coordinate-compress
        sorted_vals = sorted(vals)
        rank = {v: i+1 for i,v in enumerate(sorted_vals)}  # 1-based

        fenw = Fenwick(len(sorted_vals))
        ans = 0

        for a in A:
            # count how many prior A[i] <= a + diff
            idx = rank[a + diff]
            ans += fenw.query(idx)
            # now include this A[j] in Fenwick
            fenw.update(rank[a], 1)

        return ans
