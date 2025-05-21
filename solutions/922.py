from collections import defaultdict, deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}

        for person in range(1, n + 1):
            if person not in color:
                queue = deque([person])
                color[person] = 0
                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        if nei in color:
                            if color[nei] == color[curr]:
                                return False
                        else:
                            color[nei] = 1 - color[curr]
                            queue.append(nei)
        return True
