class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
