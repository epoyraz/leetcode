class Solution(object):
    def countKConstraintSubstrings(self, s, k, queries):
        """
        :type s: str
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        Precompute for each end j the smallest start L[j] such that substring i..j is k-valid
        iff i >= L[j]. Then for each query [l,r],
        total substrings = m*(m+1)//2 where m = r-l+1,
        minus bad reduction = sum_{j=l..r, L[j]>=l} (L[j]-l).
        Use BIT to answer sum and count over j for L[j]>=l.
        O((n+q) log n) time.
        """
        n = len(s)
        # Compute L0 and L1 via sliding windows
        L0 = [0] * n
        L1 = [0] * n
        # zeros window
        l0 = 0
        zeros = 0
        for j in range(n):
            if s[j] == '0': zeros += 1
            while zeros > k:
                if s[l0] == '0': zeros -= 1
                l0 += 1
            L0[j] = l0
        # ones window
        l1 = 0
        ones = 0
        for j in range(n):
            if s[j] == '1': ones += 1
            while ones > k:
                if s[l1] == '1': ones -= 1
                l1 += 1
            L1[j] = l1
        # L[j] = min(L0[j], L1[j])
        L = [min(L0[j], L1[j]) for j in range(n)]
        # Prepare positions by L value
        pos_by_L = [[] for _ in range(n)]
        for j, lj in enumerate(L):
            pos_by_L[lj].append(j)
        # Group queries by l
        from collections import defaultdict
        q_by_l = defaultdict(list)
        for idx, (l, r) in enumerate(queries):
            q_by_l[l].append((r, idx))
        # BIT implementation (1-indexed)
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n+1)
            def update(self, i, v):
                while i <= self.n:
                    self.bit[i] += v
                    i += i & -i
            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s
            def range_query(self, l, r):
                return self.query(r) - self.query(l-1)
        # BITs for count and sumL
        bit_cnt = BIT(n)
        bit_sum = BIT(n)
        res = [0] * len(queries)
        # process l from n-1 down to 0
        # j indices are 0-based, BIT uses j+1
        for l in range(n-1, -1, -1):
            # add all j with L[j] == l
            for j in pos_by_L[l]:
                bit_cnt.update(j+1, 1)
                bit_sum.update(j+1, l)
            # answer queries starting at l
            if l in q_by_l:
                for r, idx in q_by_l[l]:
                    m = r - l + 1
                    total = m * (m + 1) // 2
                    cnt = bit_cnt.range_query(l+1, r+1)
                    sumL = bit_sum.range_query(l+1, r+1)
                    bad = sumL - cnt * l
                    res[idx] = total - bad
        return res
