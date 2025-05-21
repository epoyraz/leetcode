from collections import defaultdict, deque

class Solution(object):
    def amountOfTime(self, root, start):
        graph = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, time + 1))

        return max_time
