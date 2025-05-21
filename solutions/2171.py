import heapq
from collections import defaultdict

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # For each node, store up to 2 distinct arrival times
        arrivals = [[] for _ in range(n + 1)]
        # Min-heap of (current_time, node)
        heap = [(0, 1)]  # start at node 1 at time 0

        while heap:
            cur_time, node = heapq.heappop(heap)

            # If we've already got two times and this one is not strictly better, skip
            times = arrivals[node]
            # Avoid duplicates
            if times and cur_time == times[-1]:
                continue
            if len(times) >= 2:
                continue

            # Record this arrival
            arrivals[node].append(cur_time)
            # If we've recorded two for target, that's the answer
            if node == n and len(arrivals[node]) == 2:
                return cur_time

            # Compute departure time after waiting for green signal if needed
            # Each signal is green for 'change' minutes, then red for 'change' minutes, repeating.
            cycle = cur_time // change
            if cycle % 2 == 1:
                # currently in a red phase
                wait = change - (cur_time % change)
                depart = cur_time + wait
            else:
                depart = cur_time

            # Traverse neighbors
            for nei in graph[node]:
                arrive_time = depart + time
                heapq.heappush(heap, (arrive_time, nei))

        # Problem guarantees a solution
        return -1
