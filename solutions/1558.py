class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        n = numCourses
        # reach[i][j] will be True if i is a prerequisite of j
        reach = [[False] * n for _ in range(n)]
        # initialize direct prerequisites
        for u, v in prerequisites:
            reach[u][v] = True
        # FloydâWarshall for transitive closure
        for k in range(n):
            for i in range(n):
                if reach[i][k]:
                    for j in range(n):
                        if reach[k][j]:
                            reach[i][j] = True
        # answer queries
        return [reach[u][v] for u, v in queries]
