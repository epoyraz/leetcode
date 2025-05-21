class Solution(object):
    def flipgame(self, fronts, backs):
        same = set()
        for f, b in zip(fronts, backs):
            if f == b:
                same.add(f)
        
        ans = float('inf')
        for x in fronts + backs:
            if x not in same:
                ans = min(ans, x)
        
        return ans if ans != float('inf') else 0
