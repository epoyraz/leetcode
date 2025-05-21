class Solution:
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        
        initial = 0
        curr = 0
        for actual, minimum in tasks:
            if curr < minimum:
                initial += (minimum - curr)
                curr = minimum
            curr -= actual
        
        return initial
