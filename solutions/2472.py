from collections import deque, defaultdict

class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        def topoSort(conds):
            indeg = [0] * (k + 1)
            adj = defaultdict(list)
            for u, v in conds:
                adj[u].append(v)
                indeg[v] += 1
            q = deque(u for u in range(1, k + 1) if indeg[u] == 0)
            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return order if len(order) == k else []

        row_order = topoSort(rowConditions)
        if not row_order:
            return []
        col_order = topoSort(colConditions)
        if not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: j for j, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            i = row_pos[num]
            j = col_pos[num]
            matrix[i][j] = num

        return matrix
