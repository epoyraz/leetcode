class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []
        
        for start, end in intervals:
            count = 0
            for x in reversed(res):
                if start <= x <= end:
                    count += 1
                if count == 2:
                    break
            needed = 2 - count
            for i in range(needed):
                res.append(end - i)
        
        return len(res)
