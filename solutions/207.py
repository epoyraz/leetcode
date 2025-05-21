class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict, deque

        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited == numCourses
