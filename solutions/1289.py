import datetime

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        date = datetime.date(year, month, day)
        return days[date.weekday()]
