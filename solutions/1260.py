class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))
        days_in_month = [31, 28 + self.is_leap(year), 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        return sum(days_in_month[:month - 1]) + day

    def is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
