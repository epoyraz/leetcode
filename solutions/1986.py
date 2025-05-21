from collections import deque

class Solution:
    def largestPathValue(self, colors, edges):
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        idx = [ord(c) - 97 for c in colors]
        dp = [[0] * 26 for _ in range(n)]
        q = deque()

        for i in range(n):
            dp[i][idx[i]] = 1
            if indegree[i] == 0:
                q.append(i)

        seen = 0
        while q:
            u = q.popleft()
            seen += 1
            for v in adj[u]:
                for c in range(26):
                    val = dp[u][c] + (1 if c == idx[v] else 0)
                    if val > dp[v][c]:
                        dp[v][c] = val
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if seen != n:
            return -1

        return max(max(row) for row in dp)
