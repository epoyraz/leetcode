class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort(reverse=True)
        total = 0
        curr = 0
        for s in satisfaction:
            if curr + s > 0:
                curr += s
                total += curr
            else:
                break
        return total
