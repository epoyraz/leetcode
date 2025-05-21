class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        
        # Union-Find setup
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        # Step 1: Sort by value, then scan nearby values to union indices
        val_with_idx = sorted((v, i) for i, v in enumerate(nums))
        for i in range(n - 1):
            v1, i1 = val_with_idx[i]
            v2, i2 = val_with_idx[i + 1]
            if abs(v1 - v2) <= limit:
                union(i1, i2)

        # Step 2: Group indices by root
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        # Step 3: For each group, sort the values and reassign to original indices
        res = nums[:]
        for indices in groups.values():
            sorted_indices = sorted(indices)
            sorted_vals = sorted(nums[i] for i in sorted_indices)
            for i, val in zip(sorted_indices, sorted_vals):
                res[i] = val

        return res
