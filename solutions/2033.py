class Solution:
    def numberOfRounds(self, loginTime, logoutTime):
        def to_minutes(t):
            h, m = map(int, t.split(":"))
            return h * 60 + m

        start = to_minutes(loginTime)
        end = to_minutes(logoutTime)

        if end < start:
            end += 24 * 60  # next day

        # round up start to the next 15-minute mark
        if start % 15 != 0:
            start += 15 - (start % 15)
        # round down end to the previous 15-minute mark
        end -= end % 15

        return max(0, (end - start) // 15)
