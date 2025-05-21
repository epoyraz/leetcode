class Solution:
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        # Days per month in a non-leap year
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        # Build prefix sum: days before the start of each month (1-indexed)
        prefix = [0]
        for d in month_days:
            prefix.append(prefix[-1] + d)
        
        def to_day_of_year(date):
            # date = "MM-DD"
            m = int(date[:2])
            d = int(date[3:])
            return prefix[m-1] + d
        
        a1 = to_day_of_year(arriveAlice)
        b1 = to_day_of_year(leaveAlice)
        a2 = to_day_of_year(arriveBob)
        b2 = to_day_of_year(leaveBob)
        
        start = max(a1, a2)
        end = min(b1, b2)
        return max(0, end - start + 1)
