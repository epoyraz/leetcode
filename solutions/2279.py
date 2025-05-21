class Solution:
    def maximumEvenSplit(self, finalSum):
        if finalSum % 2 != 0:
            return []
        
        res = []
        curr = 2
        while finalSum >= curr:
            res.append(curr)
            finalSum -= curr
            curr += 2
        
        res[-1] += finalSum
        return res
