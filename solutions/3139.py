class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n + 4
        sum_val = [0] * size          # Î£ a
        sum_sq  = [0] * size          # Î£ aÂ²
        lazy    = [0] * size

        def apply(node, l, r, d):
            length = r - l + 1
            d %= MOD
            sum_sq[node] = (sum_sq[node] + 2 * d * sum_val[node] + d * d * length) % MOD
            sum_val[node] = (sum_val[node] + d * length) % MOD
            lazy[node] = (lazy[node] + d) % MOD

        def push(node, l, r):
            if lazy[node] and l != r:
                m = (l + r) // 2
                d = lazy[node]
                apply(node * 2,     l,     m, d)
                apply(node * 2 + 1, m + 1, r, d)
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if qr < l or ql > r:
                return
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            update(node * 2,     l,     m, ql, qr)
            update(node * 2 + 1, m + 1, r, ql, qr)
            sum_val[node] = (sum_val[node * 2] + sum_val[node * 2 + 1]) % MOD
            sum_sq[node]  = (sum_sq[node  * 2] + sum_sq[node  * 2 + 1]) % MOD

        last = {}
        res  = 0
        for i, v in enumerate(nums):
            update(1, 0, n - 1, last.get(v, -1) + 1, i)
            last[v] = i
            res = (res + sum_sq[1]) % MOD
        return res
