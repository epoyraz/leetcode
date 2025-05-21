class Solution:
    def lengthOfLIS(self, nums, k):
        # We need the max value to size the segment tree
        maxv = max(nums)
        # Build iterative segment tree of size = next power of two >= maxv
        size = 1
        while size <= maxv:
            size <<= 1
        tree = [0] * (2 * size)
        
        def update(pos, val):
            # pos in [1..maxv], map to leaf at index pos-1
            idx = pos - 1 + size
            if tree[idx] >= val:
                return
            tree[idx] = val
            idx //= 2
            while idx:
                tree[idx] = max(tree[2*idx], tree[2*idx + 1])
                idx //= 2
        
        def query(l, r):
            # query max in [l..r], where l,r in [1..maxv]
            if l > r:
                return 0
            res = 0
            left = l - 1 + size
            right = r - 1 + size
            while left <= right:
                if (left & 1) == 1:
                    res = max(res, tree[left])
                    left += 1
                if (right & 1) == 0:
                    res = max(res, tree[right])
                    right -= 1
                left //= 2
                right //= 2
            return res
        
        ans = 1
        for x in nums:
            # valid previous values are in [x-k .. x-1]
            l = max(1, x - k)
            r = x - 1
            best = query(l, r)
            curr = best + 1
            update(x, curr)
            ans = max(ans, curr)
        
        return ans
