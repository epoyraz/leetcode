class Solution(object):
    def longestCycle(self, edges):
        n = len(edges)
        visited = [False] * n
        result = -1

        for i in range(n):
            if visited[i]:
                continue

            node = i
            index_map = {}
            step = 0

            while node != -1 and node not in index_map:
                if visited[node]:
                    break
                index_map[node] = step
                step += 1
                node = edges[node]

            if node != -1 and node in index_map:
                result = max(result, step - index_map[node])

            for key in index_map:
                visited[key] = True

        return result
