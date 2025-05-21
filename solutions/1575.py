class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        MOD = 10**9 + 7
        
        # Sort the cut positions
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Find maximum height between horizontal cuts (including edges)
        max_h = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        max_h = max(max_h, h - horizontalCuts[-1])
        
        # Find maximum width between vertical cuts (including edges)
        max_w = verticalCuts[0]
        for j in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[j] - verticalCuts[j-1])
        max_w = max(max_w, w - verticalCuts[-1])
        
        # The largest piece area modulo 10^9+7
        return (max_h * max_w) % MOD
