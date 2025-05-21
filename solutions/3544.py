class Solution:
    def countPairs(self, nums):
        # frequency of each number
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        vals = list(freq.keys())
        U = len(vals)
        idx = {v: i for i, v in enumerate(vals)}
        f = [freq[v] for v in vals]

        # count identical pairs
        ans = 0
        for c in f:
            ans += c * (c - 1) // 2

        # prepare digit lists
        s_list = [list(str(v)) for v in vals]

        # directed neighbors in 1 swap
        d1 = [set() for _ in range(U)]
        for u in range(U):
            s = s_list[u]
            L = len(s)
            orig = vals[u]
            for i in range(L):
                for j in range(i + 1, L):
                    t = s[:]
                    t[i], t[j] = t[j], t[i]
                    w = int(''.join(t))
                    if w != orig and w in idx:
                        d1[u].add(idx[w])

        # directed neighbors in exactly 2 swaps (excluding d1 and self)
        d2 = [set() for _ in range(U)]
        for u in range(U):
            s = s_list[u]
            L = len(s)
            orig = vals[u]
            seen = set()
            for i1 in range(L):
                for j1 in range(i1 + 1, L):
                    t1 = s[:]
                    t1[i1], t1[j1] = t1[j1], t1[i1]
                    for i2 in range(L):
                        for j2 in range(i2 + 1, L):
                            t2 = t1[:]
                            t2[i2], t2[j2] = t2[j2], t2[i2]
                            w = int(''.join(t2))
                            if w != orig and w not in seen:
                                seen.add(w)
                                v = idx.get(w)
                                if v is not None and v not in d1[u]:
                                    d2[u].add(v)

        # symmetrize to undirected adjacency
        d1u = [set() for _ in range(U)]
        d2u = [set() for _ in range(U)]
        for u in range(U):
            for v in d1[u]:
                d1u[u].add(v)
                d1u[v].add(u)
            for v in d2[u]:
                d2u[u].add(v)
                d2u[v].add(u)

        # count one-swap and two-swap pairs
        for u in range(U):
            cu = f[u]
            for v in d1u[u]:
                if u < v:
                    ans += cu * f[v]
            for v in d2u[u]:
                if u < v:
                    ans += cu * f[v]

        return ans
