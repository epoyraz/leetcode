class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = sum(salary) - min(salary) - max(salary)
        count = len(salary) - 2
        return float(total) / count
