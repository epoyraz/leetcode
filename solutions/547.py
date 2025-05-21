class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1

        return count
