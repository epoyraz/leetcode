class SegmentTree:
    def __init__(self, data):
        """
        Builds a segment tree for range maximum queries.
        data: list of initial values.
        """
        n = len(data)
        self.n = n
        # tree size 4*n is safe
        self.tree = [0] * (4 * n)
        self._build(1, 0, n - 1, data)
    
    def _build(self, node, l, r, data):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            lc = node * 2
            rc = node * 2 + 1
            self._build(lc, l, mid, data)
            self._build(rc, mid + 1, r, data)
            self.tree[node] = max(self.tree[lc], self.tree[rc])
    
    def query_first_ge(self, x):
        """
        Find the leftmost index i such that data[i] >= x.
        Returns -1 if none.
        """
        if self.tree[1] < x:
            return -1
        return self._query(1, 0, self.n - 1, x)
    
    def _query(self, node, l, r, x):
        if l == r:
            return l
        mid = (l + r) // 2
        lc = node * 2
        rc = node * 2 + 1
        # prefer left child
        if self.tree[lc] >= x:
            return self._query(lc, l, mid, x)
        else:
            return self._query(rc, mid + 1, r, x)
    
    def update(self, idx, value):
        """
        Point update: set data[idx] = value.
        """
        self._update(1, 0, self.n - 1, idx, value)
    
    def _update(self, node, l, r, idx, value):
        if l == r:
            self.tree[node] = value
        else:
            mid = (l + r) // 2
            lc = node * 2
            rc = node * 2 + 1
            if idx <= mid:
                self._update(lc, l, mid, idx, value)
            else:
                self._update(rc, mid + 1, r, idx, value)
            self.tree[node] = max(self.tree[lc], self.tree[rc])

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        st = SegmentTree(baskets)
        
        unplaced = 0
        for f in fruits:
            idx = st.query_first_ge(f)
            if idx == -1:
                # no basket can fit this fruit
                unplaced += 1
            else:
                # place fruit in basket idx; mark basket used
                st.update(idx, -1)
        return unplaced
