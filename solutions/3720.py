import collections

class Solution(object):
    def minMaxWeight(self, n, edges, threshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        # Collect unique weights
        weights = sorted({w for _, _, w in edges})
        # Build reversed adjacency lists grouped by weight threshold
        # For binary search, filter edges with w <= mid
        def can(W):
            # Build reversed graph with edges weight <= W
            adj = [[] for _ in range(n)]
            for u, v, w in edges:
                if w <= W:
                    # reversed edge v -> u
                    adj[v].append(u)
            # BFS from 0 over reversed graph
            seen = [False]*n
            dq = collections.deque([0])
            seen[0] = True
            cnt = 1
            while dq:
                x = dq.popleft()
                for y in adj[x]:
                    if not seen[y]:
                        seen[y] = True
                        cnt += 1
                        dq.append(y)
            return cnt == n
        # Binary search weights
        lo, hi = 0, len(weights)-1
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if can(weights[mid]):
                ans = weights[mid]
                hi = mid-1
            else:
                lo = mid+1
        return ans if ans is not None else -1