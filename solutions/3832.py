class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        n = len(cost)
        answer = [0] * n
        prefix_min = float('inf')
        
        for i in range(n):
            prefix_min = min(prefix_min, cost[i])
            answer[i] = prefix_min
        
        return answer
