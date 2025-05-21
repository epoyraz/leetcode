class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
        
        ans = [-1] * n

        def dfs(x):
            if ans[x] != -1:
                return ans[x]
            ans[x] = x
            for y in graph[x]:
                cand = dfs(y)
                if quiet[cand] < quiet[ans[x]]:
                    ans[x] = cand
            return ans[x]
        
        for i in range(n):
            dfs(i)
        
        return ans
