class Solution(object):
    def checkWays(self, pairs):
        from collections import defaultdict

        # 1) Build adjacency and collect all distinct nodes
        adj = defaultdict(set)
        nodes = set()
        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
            nodes.add(x)
            nodes.add(y)
        n = len(nodes)

        # 2) Compute degrees
        deg = {u: len(adj[u]) for u in nodes}

        # 3) Identify root candidates: must connect to all other nodes
        maxdeg = n - 1
        roots = [u for u in nodes if deg[u] == maxdeg]
        # If no node has degree n-1, impossible to have a root ancestor of all â 0 ways
        if not roots:
            return 0
        # If more than one node has degree n-1, there are at least 2 choices of root â at least 2 ways
        ways = 1 if len(roots) == 1 else 2
        chosen_root = roots[0]  # pick any one to run the check for consistency

        # 4) For each non-root node, pick its parent among its neighbors
        #    The parent must have degree â¥ deg[u], and among those the smallest such degree.
        for u in nodes:
            if u == chosen_root:
                continue
            best_parent = None
            best_deg = float('inf')
            for v in adj[u]:
                if deg[v] >= deg[u] and deg[v] < best_deg:
                    best_parent = v
                    best_deg = deg[v]
            # If we found no valid parent, it's impossible
            if best_parent is None:
                return 0

            # 5) Check that u's entire neighborâset (except the parent) 
            #    is a subset of best_parent's neighborâset.
            #    This enforces that every neighbor of u is indeed an ancestor or descendant
            #    correctly nested under best_parent in the rooted tree.
            for v in adj[u]:
                if v is best_parent:
                    continue
                if v not in adj[best_parent]:
                    return 0

            # 6) If deg[parent] == deg[u], swapping parent/child roles still satisfies
            #    all adjacency constraints â multiple valid trees.
            if deg[best_parent] == deg[u]:
                ways = 2

        return ways
