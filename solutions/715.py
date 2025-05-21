import bisect

class RangeModule(object):

    def __init__(self):
        # List of non-overlapping, sorted intervals [start, end)
        self.intervals = []

    def addRange(self, left, right):
        """
        Adds [left, right), merging overlapping intervals.
        """
        intervals = self.intervals
        # Find the position to insert
        i = bisect.bisect_left(intervals, [left, 0])
        # If there is an interval before i that overlaps, include it
        if i > 0 and intervals[i-1][1] >= left:
            i -= 1
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
        # Merge all intervals that overlap [left, right)
        j = i
        while j < len(intervals) and intervals[j][0] <= right:
            right = max(right, intervals[j][1])
            j += 1
        # Replace intervals[i:j] with the merged interval
        intervals[i:j] = [[left, right]]

    def queryRange(self, left, right):
        """
        Returns True if every point in [left, right) is covered.
        """
        intervals = self.intervals
        # Find the first interval with start > left
        i = bisect.bisect_right(intervals, [left, float('inf')])
        # The covering interval, if it exists, must be intervals[i-1]
        if i == 0:
            return False
        return intervals[i-1][1] >= right

    def removeRange(self, left, right):
        """
        Removes coverage of [left, right) by splitting intervals as needed.
        """
        intervals = self.intervals
        new_intervals = []
        for start, end in intervals:
            # No overlap
            if end <= left or start >= right:
                new_intervals.append([start, end])
            else:
                # Left piece remains
                if start < left:
                    new_intervals.append([start, left])
                # Right piece remains
                if end > right:
                    new_intervals.append([right, end])
        self.intervals = new_intervals
