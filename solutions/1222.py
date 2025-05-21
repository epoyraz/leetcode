class Solution:
    def removeCoveredIntervals(self, intervals):
        # Sort by start ascending, and end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        prev_end = 0
        
        for start, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end  # Update to current end
            # else: interval is covered
        
        return count
