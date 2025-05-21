class SummaryRanges(object):
    def __init__(self):
        self.nums = set()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.add(value)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(self.nums)
        res = []
        for num in sorted_nums:
            if not res or res[-1][1] + 1 < num:
                res.append([num, num])
            else:
                res[-1][1] = num
        return res
