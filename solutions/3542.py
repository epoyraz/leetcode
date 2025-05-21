import heapq

class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        N      = m + n + 2          # total vertices
        SRC    = m + n               # super-source index
        SINK   = m + n + 1           # super-sink   index
        INF    = 10 ** 18

        # adjacency lists: [to, cap, cost, rev_index]
        g = [[] for _ in xrange(N)]

        def add(u, v, cap, cost):
            g[u].append([v, cap, cost, len(g[v])])
            g[v].append([u, 0,  -cost, len(g[u]) - 1])

        # source â rows
        for i in xrange(m):
            add(SRC, i, 1, 0)
        # columns â sink
        for j in xrange(n):
            add(m + j, SINK, 1, 0)
        # row â column edges (negative cost = âvalue)
        for i in xrange(m):
            row = board[i]
            ri  = i
            for j in xrange(n):
                add(ri, m + j, 1, -row[j])

        h      = [0] * N               # Johnson potentials
        dist   = [0] * N
        prev_v = [0] * N
        prev_e = [0] * N
        flow   = 0
        cost   = 0

        while flow < 3:                 # we only need three augmentations
            for v in xrange(N):
                dist[v] = INF
            dist[SRC] = 0
            pq = [(0, SRC)]

            # Dijkstra with reduced costs
            while pq:
                d, v = heapq.heappop(pq)
                if d != dist[v]:
                    continue
                for idx, e in enumerate(g[v]):
                    to, cap, c, _ = e
                    if cap and dist[to] > d + c + h[v] - h[to]:
                        dist[to]  = d + c + h[v] - h[to]
                        prev_v[to] = v
                        prev_e[to] = idx
                        heapq.heappush(pq, (dist[to], to))

            if dist[SINK] == INF:           # should never happen (board â¥ 3Ã3)
                break

            for v in xrange(N):             # update potentials
                if dist[v] < INF:
                    h[v] += dist[v]

            add_flow = 3 - flow             # remaining units to push (â¤ 1)
            v = SINK
            while v != SRC:
                u  = prev_v[v]
                e  = g[u][prev_e[v]]
                if add_flow > e[1]:
                    add_flow = e[1]
                v = u

            flow += add_flow
            cost += add_flow * h[SINK]

            # augment along the path
            v = SINK
            while v != SRC:
                u   = prev_v[v]
                e   = g[u][prev_e[v]]
                e[1]           -= add_flow
                g[v][e[3]][1]  += add_flow
                v = u

        return -cost                   # negate to obtain the maximum sum
