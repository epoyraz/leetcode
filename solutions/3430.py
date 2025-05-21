class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days

        # Sort meetings by start time
        meetings.sort()
        
        merged = []
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        # Total days covered by meetings
        meeting_days = sum(end - start + 1 for start, end in merged)
        
        return days - meeting_days
