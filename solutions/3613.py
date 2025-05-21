class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        from collections import defaultdict, deque

        def build_graph(pairs, rates):
            # undirected adjacency: u->v with w, v->u with 1/w
            g = defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                g[u].append((v, r))
                g[v].append((u, 1.0/r))
            return g

        def bfs_best(start, graph):
            # returns dict best[x] = product along unique path start->x
            best = {start: 1.0}
            q = deque([start])
            while q:
                u = q.popleft()
                for v, r in graph[u]:
                    if v not in best:
                        best[v] = best[u] * r
                        q.append(v)
            return best

        # 1) build day1 and day2 graphs
        g1 = build_graph(pairs1, rates1)
        g2 = build_graph(pairs2, rates2)

        # 2) compute best1[C] for day1 from initial
        best1 = bfs_best(initialCurrency, g1)
        # 3) compute best2[C] for day2 from initial
        best2 = bfs_best(initialCurrency, g2)

        # 4) maximize best1[C] / best2[C] over currencies reachable in both
        ans = 1.0  # at worst do nothing
        for C, amt1 in best1.items():
            if C in best2:
                cand = amt1 / best2[C]
                if cand > ans:
                    ans = cand

        return ans
