from collections import deque, defaultdict

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(patience)
        dist = [0] * n
        visited = [False] * n

        # Step 2: BFS to find shortest distance from node 0
        queue = deque()
        queue.append(0)
        visited[0] = True
        level = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                dist[node] = level
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            level += 1

        # Step 3: Compute max time any reply is received
        max_time = 0
        for i in range(1, n):
            round_trip = 2 * dist[i]
            if patience[i] >= round_trip:
                last_time = round_trip
            else:
                last_sent = ((round_trip - 1) // patience[i]) * patience[i]
                last_time = last_sent + round_trip
            if last_time > max_time:
                max_time = last_time

        return max_time + 1
