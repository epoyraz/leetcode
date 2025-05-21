class SegTree:
    def __init__(self, data):
        n = len(data)
        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        self.lazy = [False] * (2 * size)
        for i, v in enumerate(data):
            self.tree[size + i] = v
        for i in range(size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def _apply(self, idx, length):
        self.tree[idx] = length - self.tree[idx]
        self.lazy[idx] = not self.lazy[idx]

    def _push(self, idx, length):
        if self.lazy[idx]:
            mid = length // 2
            self._apply(2 * idx, mid)
            self._apply(2 * idx + 1, length - mid)
            self.lazy[idx] = False

    def _update(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.tree[idx] = (r - l + 1) - self.tree[idx]
            self.lazy[idx] = not self.lazy[idx]
            return
        self._push(idx, r - l + 1)
        m = (l + r) // 2
        self._update(2 * idx, l, m, ql, qr)
        self._update(2 * idx + 1, m + 1, r, ql, qr)
        self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def update(self, l, r):
        self._update(1, 0, self.size - 1, l, r)

    def query(self, l, r):
        return self._query(1, 0, self.size - 1, l, r)

    def _query(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[idx]
        self._push(idx, r - l + 1)
        m = (l + r) // 2
        return self._query(2 * idx, l, m, ql, qr) + self._query(2 * idx + 1, m + 1, r, ql, qr)


class Solution:
    def handleQuery(self, nums1, nums2, queries):
        n = len(nums1)
        st = SegTree(nums1)
        total = sum(nums2)
        ans = []
        for typ, x, y in queries:
            if typ == 1:
                st.update(x, y)
            elif typ == 2:
                cnt1 = st.query(0, n - 1)
                total += cnt1 * x
            else:
                ans.append(total)
        return ans
