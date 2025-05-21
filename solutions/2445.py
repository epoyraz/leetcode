class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        restricted_set = set(restricted)
        visited = set()
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([0])
        visited.add(0)
        count = 0

        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                if nei not in visited and nei not in restricted_set:
                    visited.add(nei)
                    queue.append(nei)
        
        return count
