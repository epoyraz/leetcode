import bisect

class CountIntervals:
    def __init__(self):
        # Sorted lists of interval starts and ends (inclusive)
        self.starts = []
        self.ends = []
        self.total = 0

    def add(self, left, right):
        # We'll merge [left, right] with any overlapping intervals
        s, e = left, right
        # Find insertion point
        i = bisect.bisect_left(self.starts, s)
        
        # Check if the previous interval overlaps or is adjacent
        if i > 0 and self.ends[i-1] >= s - 1:
            i -= 1
        
        # Merge forward through all overlapping/adjacent intervals
        j = i
        while j < len(self.starts) and self.starts[j] <= e + 1:
            # Expand our merged interval
            s = min(s, self.starts[j])
            e = max(e, self.ends[j])
            # Subtract out the old interval's covered length
            self.total -= (self.ends[j] - self.starts[j] + 1)
            j += 1
        
        # Remove the intervals we've merged [i:j]
        if j > i:
            del self.starts[i:j]
            del self.ends[i:j]
        
        # Insert the merged interval
        self.starts.insert(i, s)
        self.ends.insert(i, e)
        # Add its coverage
        self.total += (e - s + 1)

    def count(self):
        return self.total
