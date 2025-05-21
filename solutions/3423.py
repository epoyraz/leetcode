class Solution(object):
    def maximumSumSubsequence(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        NEG_INF = -10**18

        # merge two DP-states in O(1)
        def merge(A, B):
            A00, A01, A10, A11 = A
            B00, B01, B10, B11 = B
            C00 = max(A00 + B00, A00 + B10, A01 + B00)
            C01 = max(A00 + B01, A00 + B11, A01 + B01)
            C10 = max(A10 + B00, A10 + B10, A11 + B00)
            C11 = max(A10 + B01, A10 + B11, A11 + B01)
            return (C00, C01, C10, C11)

        # tree will hold 4*n nodes
        tree = [None] * (4 * n)

        # build the segment tree over [l..r]
        def build(node, l, r):
            if l == r:
                v = nums[l]
                # leaf: you either pick nothing (00â0) or pick v (11âv)
                tree[node] = (0, NEG_INF, NEG_INF, v)
            else:
                mid = (l + r) // 2
                build(node*2,     l,   mid)
                build(node*2 + 1, mid+1, r)
                tree[node] = merge(tree[node*2], tree[node*2 + 1])

        # pointâupdate
        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = (0, NEG_INF, NEG_INF, val)
            else:
                mid = (l + r) // 2
                if idx <= mid:
                    update(node*2,     l,   mid, idx, val)
                else:
                    update(node*2 + 1, mid+1, r, idx, val)
                tree[node] = merge(tree[node*2], tree[node*2 + 1])

        # build once
        build(1, 0, n-1)

        ans = 0
        for pos, x in queries:
            update(1, 0, n-1, pos, x)
            # after each update, the root (node 1) holds the 4 states for [0..n-1]
            ans = (ans + max(tree[1])) % MOD

        return ans
