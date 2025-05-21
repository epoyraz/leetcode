class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        Computes the minimum number of months needed to complete all courses given prerequisite relations
        and individual course durations. Multiple courses may be taken in parallel as long as prerequisites
        are met.

        :param n: int, number of courses labeled from 1 to n
        :param relations: List[List[int]], each pair [u, v] means u must be completed before v
        :param time: List[int], time[i] is the duration to complete course i+1
        :return: int, minimum months to finish all courses
        """
        from collections import deque, defaultdict

        # Build adjacency list and in-degree counts
        graph = defaultdict(list)
        indegree = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            indegree[v] += 1

        # dp[i] tracks earliest completion time of course i
        dp = [0] * (n + 1)

        # Initialize queue with courses without prerequisites
        q = deque()
        for course in range(1, n + 1):
            if indegree[course] == 0:
                dp[course] = time[course - 1]
                q.append(course)

        # Process courses in topological order
        while q:
            u = q.popleft()
            for v in graph[u]:
                # v can only start after u is completed
                dp[v] = max(dp[v], dp[u] + time[v - 1])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # The answer is the maximum completion time among all courses
        return max(dp[1:])