class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        # collect all teams with no incoming edges
        sources = [i for i in range(n) if indegree[i] == 0]
        # if exactly one, that's the unique champion; otherwise no unique champion
        return sources[0] if len(sources) == 1 else -1