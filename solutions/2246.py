from collections import defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        # longest chain ending at each node
        longest = [0] * n
        queue = deque(i for i in range(n) if indegree[i] == 0)

        while queue:
            u = queue.popleft()
            v = favorite[u]
            longest[v] = max(longest[v], longest[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

        visited = [False] * n
        max_cycle = 0
        mutual_sum = 0

        for i in range(n):
            if visited[i] or indegree[i] == 0:
                continue

            # detect cycle
            curr = i
            cycle = []
            while not visited[curr]:
                visited[curr] = True
                cycle.append(curr)
                curr = favorite[curr]

            # check if it's a mutual pair
            if len(cycle) == 2 and favorite[cycle[1]] == cycle[0]:
                mutual_sum += 2 + longest[cycle[0]] + longest[cycle[1]]
            else:
                max_cycle = max(max_cycle, len(cycle))

        return max(max_cycle, mutual_sum)
