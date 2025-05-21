from collections import defaultdict

class Solution:
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        # Build graph and track in/out degrees
        adj = defaultdict(list)
        out_deg = defaultdict(int)
        in_deg = defaultdict(int)
        
        for u, v in pairs:
            adj[u].append(v)
            out_deg[u] += 1
            in_deg[v] += 1
        
        # Find start node: out_deg - in_deg = 1, if none, pick any u
        start = None
        for node in adj:
            if out_deg[node] - in_deg[node] == 1:
                start = node
                break
        if start is None:
            # Eulerian cycle case: start anywhere with outgoing edge
            start = pairs[0][0]
        
        # Hierholzer's algorithm to find Eulerian path
        stack = [start]
        path = []  # will hold nodes in reverse of the final path
        while stack:
            u = stack[-1]
            if adj[u]:
                v = adj[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())
        
        # path is reversed list of vertices; reverse it
        path.reverse()
        
        # Build edge list from consecutive vertices
        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i+1]])
        
        return result
