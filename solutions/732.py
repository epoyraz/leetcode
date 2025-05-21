from collections import Counter

class MyCalendarThree(object):
    def __init__(self):
        self.delta = Counter()

    def book(self, startTime, endTime):
        self.delta[startTime] += 1
        self.delta[endTime] -= 1
        curr = 0
        res = 0
        for t in sorted(self.delta):
            curr += self.delta[t]
            res = max(res, curr)
        return res