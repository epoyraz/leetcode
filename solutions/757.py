class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b, c in allowed:
            graph[(a, b)].append(c)
        
        def dfs(row):
            if len(row) == 1:
                return True
            next_rows = []
            for i in range(len(row) - 1):
                pair = (row[i], row[i+1])
                if pair not in graph:
                    return False
                next_rows.append(graph[pair])
            
            def backtrack(path, idx):
                if idx == len(next_rows):
                    return dfs(path)
                for ch in next_rows[idx]:
                    if backtrack(path + ch, idx + 1):
                        return True
                return False
            
            return backtrack('', 0)
        
        return dfs(bottom)
