class Solution(object):
    def crackSafe(self, n, k):
        seen = set()
        ans = []
        
        def dfs(node):
            for x in range(k):
                nei = node + str(x)
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(str(x))
        
        dfs('0' * (n-1))
        return ''.join(ans) + '0' * (n-1)
