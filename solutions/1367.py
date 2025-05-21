class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        # 1. Normalize: sort dimensions of each cuboid so that d0 <= d1 <= d2
        for c in cuboids:
            c.sort()
        # 2. Sort cuboids lexicographically by (d0, d1, d2)
        cuboids.sort()
        
        n = len(cuboids)
        # dp[i]: max stack height ending with cuboid i on top
        dp = [0] * n
        ans = 0
        
        for i in range(n):
            # standalone height is its own d2
            dp[i] = cuboids[i][2]
            # try placing it on any previous cuboid j
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            ans = max(ans, dp[i])
        
        return ans
