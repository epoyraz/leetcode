class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return sum(h >= target for h in hours)
