class Solution(object):
    def taskSchedulerII(self, tasks, space):
        last_day = {}
        day = 0

        for t in tasks:
            if t in last_day and day - last_day[t] <= space:
                day = last_day[t] + space + 1
            else:
                day += 1
            last_day[t] = day

        return day
