class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Initialize an array to track the indegree of each vertex
        indegree = [0] * n

        # Calculate indegree for each vertex
        for u, v in edges:
            indegree[v] += 1

        # Collect all vertices with indegree 0 (source vertices)
        result = [i for i in range(n) if indegree[i] == 0]

        return result
