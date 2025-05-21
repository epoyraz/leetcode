class SegmentTree:
    def __init__(self, data, k):
        """
        data: list of initial values
        k: the modulus
        """
        self.n = len(data)
        self.k = k
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        # Each node stores (prod, cnt_list)
        # We'll use 1-indexed tree array of length 2*self.size
        self.tree = [None] * (2*self.size)
        # Build leaves
        for i in range(self.size):
            if i < self.n:
                pv = data[i] % k
                cnt = [0]*k
                cnt[pv] = 1
                self.tree[self.size + i] = (pv, cnt)
            else:
                # dummy beyond n: treat as empty segment (prod=1, no prefixes)
                self.tree[self.size + i] = (1, [0]*k)
        # Build internal nodes
        for idx in range(self.size-1, 0, -1):
            self.tree[idx] = self._merge(self.tree[2*idx], self.tree[2*idx+1])

    def _merge(self, left, right):
        """Merge two nodes (prodL, cntL), (prodR, cntR)."""
        prodL, cntL = left
        prodR, cntR = right
        k = self.k
        # combined product
        prod = (prodL * prodR) % k
        # combined counts
        cnt = [0]*k
        # 1) all prefixes entirely in L
        for t in range(k):
            cnt[t] += cntL[t]
        # 2) prefixes that cross into R:
        #    if a prefix of R has remainder b, 
        #    when multiplied by whole-L, becomes (prodL * b)%k
        for b in range(k):
            if cntR[b]:
                t = (prodL * b) % k
                cnt[t] += cntR[b]
        return (prod, cnt)

    def point_update(self, pos, value):
        """
        Set data[pos] = value, and update up the tree.
        """
        k = self.k
        i = self.size + pos
        pv = value % k
        cnt = [0]*k
        cnt[pv] = 1
        self.tree[i] = (pv, cnt)
        # climb
        i //= 2
        while i:
            self.tree[i] = self._merge(self.tree[2*i], self.tree[2*i+1])
            i //= 2

    def range_query(self, left, right):
        """
        Query the merged node for interval [left..right], inclusive.
        """
        k = self.k
        # We'll merge from left to right, so we keep two accumulators:
        # one for the result built so far (res_prod, res_cnt),
        # initially empty segment: prod=1, cnt=zeros
        res_prod, res_cnt = 1, [0]*k
        # We'll do the standard two-pointer on the segment tree:
        l = left + self.size
        r = right + self.size
        # To preserve order, we need to collect the nodes in two lists:
        left_nodes = []
        right_nodes = []
        while l <= r:
            if (l & 1) == 1:
                left_nodes.append(l)
                l += 1
            if (r & 1) == 0:
                right_nodes.append(r)
                r -= 1
            l //= 2; r //= 2
        # First merge all left_nodes in order, then right_nodes in reverse order:
        for idx in left_nodes + right_nodes[::-1]:
            node_prod, node_cnt = self.tree[idx]
            # merge (res_prod, res_cnt) with this node:
            # new_prod = res_prod * node_prod
            new_cnt = [0]*k
            # prefixes entirely in accumulated
            for t in range(k):
                new_cnt[t] += res_cnt[t]
            # prefixes that cross into the new node:
            for b in range(k):
                if node_cnt[b]:
                    t = (res_prod * b) % k
                    new_cnt[t] += node_cnt[b]
            res_prod = (res_prod * node_prod) % k
            res_cnt = new_cnt
        return res_prod, res_cnt

class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        st = SegmentTree(nums, k)
        ans = []
        for idx, val, start, x in queries:
            # 1) persistent update
            st.point_update(idx, val)
            # 2) query suffix [start..n-1]
            _, cnt = st.range_query(start, len(nums)-1)
            # number of prefixes whose product â¡ x mod k
            ans.append(cnt[x])
        return ans
