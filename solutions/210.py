from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0] * numCourses
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return res if len(res) == numCourses else []
