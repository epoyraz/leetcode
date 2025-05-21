class Solution:
    def validSubarraySize(self, nums, threshold):
        n = len(nums)
        
        # Disjoint Set Union to track lengths of active segments
        parent = list(range(n))
        size = [0] * n
        active = [False] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return ra
            # merge smaller into larger
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return ra
        
        # Group indices by value
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        # Process distinct values in descending order
        for v in sorted(pos.keys(), reverse=True):
            # compute needed subarray length for this value
            k_needed = threshold // v + 1
            
            # activate all positions with value == v
            for i in pos[v]:
                active[i] = True
                parent[i] = i
                size[i] = 1
                # merge with left neighbor if active
                if i > 0 and active[i-1]:
                    ri = union(i, i-1)
                    # size[ri] updated in union
                # merge with right neighbor if active
                if i+1 < n and active[i+1]:
                    ri = union(i, i+1)
                # after unions, check the component size
                root = find(i)
                if size[root] >= k_needed:
                    return k_needed
        
        # no valid subarray found
        return -1
