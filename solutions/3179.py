class Solution:
    def maximumPoints(self, edges, coins, k):
        n = len(coins)
        # compute how many halvings are ever meaningful
        H = max(coins).bit_length() + 1

        # build the rooted tree at 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1]*n
        parent[0] = 0
        order = [0]
        for u in order:                  # simple BFS/DFS to orient edges
            for v in adj[u]:
                if parent[v] < 0:
                    parent[v] = u
                    order.append(v)

        # build children lists
        children = [[] for _ in range(n)]
        for u in range(1, n):
            children[parent[u]].append(u)

        # dp[u][h] = best score in u's subtree if u has already been halved h times
        dp = [[0]*(H+1) for _ in range(n)]

        # process in reverseâorder (leaf â root)
        for u in reversed(order):
            for h in range(H+1):
                # current coins at u after h halvings
                cur = coins[u] >> h

                # sum of dp[v][h] or dp[v][h+1] over children
                sumA = sum(dp[v][h] for v in children[u])
                sumB = sum(dp[v][h+1] if h+1 <= H else dp[v][H]
                           for v in children[u])

                # option1: take all current coins, pay k
                opt1 = (cur - k) + sumA
                # option2: take half, introduce an extra halving for descendants
                opt2 = (cur >> 1) + sumB

                dp[u][h] = max(opt1, opt2)

        return dp[0][0]
