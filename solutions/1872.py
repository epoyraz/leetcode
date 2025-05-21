class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(candiesCount)
        
        # Step 1: Build prefix sum of candiesCount
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + candiesCount[i]
        
        res = []
        for t, d, cap in queries:
            minCandiesEaten = d + 1
            maxCandiesEaten = (d + 1) * cap
            # Check overlap between [prefixSum[t] + 1, prefixSum[t+1]]
            canEat = maxCandiesEaten > prefixSum[t] and minCandiesEaten <= prefixSum[t + 1]
            res.append(canEat)
        
        return res
