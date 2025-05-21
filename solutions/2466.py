class Solution(object):
    def maximumSegmentSum(self, nums, removeQueries):
        n = len(nums)
        res = [0] * n
        parent = list(range(n))
        seg_sum = [0] * n
        active = [False] * n
        max_sum = 0

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n - 1, -1, -1):
            idx = removeQueries[i]
            active[idx] = True
            seg_sum[idx] = nums[idx]

            if idx > 0 and active[idx - 1]:
                left = find(idx - 1)
                parent[idx] = left
                seg_sum[left] += seg_sum[idx]
                seg_sum[idx] = 0

            if idx < n - 1 and active[idx + 1]:
                right = find(idx + 1)
                root = find(idx)
                if root != right:
                    parent[right] = root
                    seg_sum[root] += seg_sum[right]
                    seg_sum[right] = 0

            max_sum = max(max_sum, seg_sum[find(idx)])
            if i > 0:
                res[i - 1] = max_sum

        return res
