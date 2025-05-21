from collections import deque

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Build initial chain 0â1â2ââ¦ânâ1
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            adj[i].append(i+1)

        ans = []
        for u, v in queries:
            # add the new shortcut
            adj[u].append(v)

            # BFS from 0
            dist = [-1]*n
            dq = deque([0])
            dist[0] = 0
            while dq:
                x = dq.popleft()
                if x == n-1:
                    break
                for y in adj[x]:
                    if dist[y] < 0:
                        dist[y] = dist[x] + 1
                        dq.append(y)

            ans.append(dist[n-1])
        return ans
