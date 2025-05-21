class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # Number of nodes
        n = len(edges) + 1
        
        # Build undirected adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Root the tree at 0: compute parent and DFS order
        parent = [-1] * n
        parent[0] = 0
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        
        # Build children lists
        children = [[] for _ in range(n)]
        for v in range(1, n):
            p = parent[v]
            children[p].append(v)
        
        # Compute subtree sizes in reverse DFS order
        subtree_size = [1] * n
        for u in reversed(order):
            for w in children[u]:
                subtree_size[u] += subtree_size[w]
        
        # Count "good" nodes
        # A node is good if all its children's subtree sizes are equal
        count = 0
        for u in range(n):
            sizes = [subtree_size[w] for w in children[u]]
            # zero or one child always trivially equal
            if len(sizes) <= 1 or all(sz == sizes[0] for sz in sizes):
                count += 1
        
        return count
