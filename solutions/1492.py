class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        from collections import defaultdict

        tree = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        def dfs(emp):
            if not tree[emp]:
                return 0
            return informTime[emp] + max(dfs(sub) for sub in tree[emp])

        return dfs(headID)
