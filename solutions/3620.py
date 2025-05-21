class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Build list of intervals [a-k, a+k] for each element a.
        intervals = [(a - k, a + k) for a in nums]
        # Sort by right endpoint
        intervals.sort(key=lambda x: x[1])

        parent = {}  # for union-find ânext freeâ pointers

        def find(x):
            # Return smallest integer â¥ x that is not yet occupied
            if x not in parent:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def occupy(x):
            # Mark x as used, so next time find(x) returns â¥ x+1
            parent[x] = x + 1

        matches = 0
        for L, R in intervals:
            x = find(L)
            if x <= R:
                occupy(x)
                matches += 1

        return matches
