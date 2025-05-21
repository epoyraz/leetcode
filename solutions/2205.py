class Solution:
    def goodDaysToRobBank(self, security, time):
        n = len(security)
        # If time == 0, every day is good
        if time == 0:
            return list(range(n))
        
        # left[i]: number of consecutive non-increasing days ending at i
        left = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
        
        # right[i]: number of consecutive non-decreasing days starting at i
        right = [0] * n
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                right[i] = right[i+1] + 1
        
        res = []
        # A good day i needs at least 'time' before and after
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                res.append(i)
        
        return res
