class Solution:
    def getAncestors(self, n, edgeList):
        # Step 1: Build the adjacency list for the graph
        graph = [[] for _ in range(n)]
        for from_node, to_node in edgeList:
            graph[to_node].append(from_node)  # reverse edges for easier ancestor finding
        
        # Step 2: Cache to store the ancestors of each node
        ancestors_cache = {}

        # Step 3: DFS function to find ancestors of a node
        def dfs(node):
            if node in ancestors_cache:
                return ancestors_cache[node]
            
            # Start with an empty set of ancestors
            ancestors = set()
            for parent in graph[node]:
                ancestors.add(parent)  # add the immediate parent
                ancestors.update(dfs(parent))  # add ancestors of the parent recursively
            
            ancestors_cache[node] = ancestors
            return ancestors
        
        # Step 4: Find ancestors for all nodes
        result = []
        for i in range(n):
            result.append(sorted(list(dfs(i))))  # Get ancestors for node i and sort them
            
        return result