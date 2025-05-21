from collections import deque, defaultdict

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        RED, BLUE = 0, 1
        graph = [defaultdict(list), defaultdict(list)]  # 0: red, 1: blue
        
        for u, v in redEdges:
            graph[RED][u].append(v)
        for u, v in blueEdges:
            graph[BLUE][u].append(v)
        
        # dist[node][color] = shortest distance to node ending with given color edge
        dist = [[-1, -1] for _ in range(n)]
        dist[0] = [0, 0]  # distance to node 0 is 0 for both colors

        queue = deque()
        queue.append((0, RED))
        queue.append((0, BLUE))

        while queue:
            node, color = queue.popleft()
            next_color = 1 - color
            for nei in graph[next_color][node]:
                if dist[nei][next_color] == -1:
                    dist[nei][next_color] = dist[node][color] + 1
                    queue.append((nei, next_color))

        res = []
        for red_d, blue_d in dist:
            if red_d == -1 or blue_d == -1:
                res.append(max(red_d, blue_d))
            else:
                res.append(min(red_d, blue_d))
        return res
