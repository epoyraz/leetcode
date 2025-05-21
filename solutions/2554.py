import sys
import heapq

class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort(key=lambda x: x[0])
        n = len(robot)
        # Initialize dp: dp[r] = min cost to fix first r robots
        INF = 10**30
        dp = [INF] * (n + 1)
        dp[0] = 0
        # For each factory, update dp
        for pos, limit in factory:
            # cost to assign t robots ending at r to this factory
            # precompute prefix sums of distances
            dist = [0] * (n + 1)
            for i in range(1, n + 1):
                dist[i] = dist[i-1] + abs(robot[i-1] - pos)
            # new dp copy
            new_dp = dp[:]
            # try assigning t robots to this factory
            for r in range(1, n + 1):
                # assign t robots ending at r
                for t in range(1, min(limit, r) + 1):
                    cost = dp[r-t] + (dist[r] - dist[r-t])
                    if cost < new_dp[r]:
                        new_dp[r] = cost
            dp = new_dp
        # answer: all n robots
        return dp[n]