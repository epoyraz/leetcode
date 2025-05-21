import heapq

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for idx, (u, v, w) in enumerate(edges):
            adj[u].append((v, idx))
            adj[v].append((u, idx))

        INF = 10**18
        MAXW = 2 * 10**9

        # 1) Compute the shortest distance if every â1 edge had weight = 1
        def dijkstra_min():
            dist = [INF] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, idx in adj[u]:
                    w = edges[idx][2]
                    cost = w if w != -1 else 1
                    nd = d + cost
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        dist_min = dijkstra_min()[destination]
        if dist_min > target:
            return []  # even with all â1 set to 1, path too long

        # 2) Compute the shortest distance if every â1 edge is unusable (weight = INF)
        def dijkstra_fixed(start):
            dist = [INF] * n
            dist[start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, idx in adj[u]:
                    w = edges[idx][2]
                    cost = w if w != -1 else INF
                    nd = d + cost
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        dist_fixed = dijkstra_fixed(source)[destination]
        if dist_fixed < target:
            return []  # even ignoring â1 edges, path is too short

        # 3) If fixed-only path equals target, assign all â1 edges to a large weight
        if dist_fixed == target:
            result = []
            for u, v, w in edges:
                if w == -1:
                    result.append([u, v, MAXW])
                else:
                    result.append([u, v, w])
            return result

        # 4) Otherwise, we know dist_min <= target < dist_fixed.
        #    Compute dist_to_dest ignoring â1 edges for slack calculation.
        dist_to_dest = [INF] * n
        dist_to_dest[destination] = 0
        pq = [(0, destination)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist_to_dest[u]:
                continue
            for v, idx in adj[u]:
                w = edges[idx][2]
                cost = w if w != -1 else INF
                nd = d + cost
                if nd < dist_to_dest[v]:
                    dist_to_dest[v] = nd
                    heapq.heappush(pq, (nd, v))

        # 5) Run Dijkstra from source, dynamically assigning â1 edges to meet the target
        dist = [INF] * n
        dist[source] = 0
        assign = {}  # idx -> assigned weight for â1 edges
        pq = [(0, source)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, idx in adj[u]:
                orig = edges[idx][2]
                if orig != -1:
                    cost = orig
                else:
                    # choose x so that d + x + dist_to_dest[v] == target
                    slack = target - d - dist_to_dest[v]
                    cost = slack if slack > 1 else 1
                nd = d + cost
                if nd < dist[v] and nd <= target:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
                    if orig == -1:
                        assign[idx] = cost

        if dist[destination] != target:
            return []  # could not make it exactly target

        # 6) Build the answer, using assigned weights for used â1 edges,
        #    and MAXW for all other â1 edges
        result = []
        for idx, (u, v, w) in enumerate(edges):
            if w == -1:
                w_new = assign.get(idx, MAXW)
                result.append([u, v, w_new])
            else:
                result.append([u, v, w])
        return result
