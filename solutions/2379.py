class Solution:
    def maximumImportance(self, n, roads):
        # 1) Compute degrees
        deg = [0]*n
        for u,v in roads:
            deg[u] += 1
            deg[v] += 1
        
        # 2) Sort degrees ascending
        deg.sort()
        
        # 3) Assign values 1..n to degrees in sorted order
        ans = 0
        for i, d in enumerate(deg):
            ans += d * (i+1)
        
        return ans
