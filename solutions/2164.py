import bisect

class Solution:
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # Sort events by start time
        events.sort(key=lambda e: e[0])
        starts = [e[0] for e in events]
        n = len(events)
        
        # Build suffix-max array of single-event values
        # suffix_max[i] = max value of any event in events[i:]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])
        
        ans = 0
        # Try taking each event as the first one
        for i, (s, e, v) in enumerate(events):
            # Option 1: take only this event
            ans = max(ans, v)
            
            # Option 2: take this event + best non-overlapping one
            # find first event whose start > e
            j = bisect.bisect_right(starts, e)
            if j < n:
                ans = max(ans, v + suffix_max[j])
        
        return ans
