class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Build component ids: consecutive nums with gap <= maxDiff are connected.
        comp = [0] * n
        for i in range(1, n):
            # if this node links to the previous one, share component;
            # otherwise start a new component.
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1
        
        # For each query, they're connected iff in the same component.
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
        return ans
