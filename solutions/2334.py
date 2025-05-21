from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers, people):
        # Extract and sort all start and end times
        starts = sorted(s for s, e in flowers)
        ends   = sorted(e for s, e in flowers)
        
        ans = []
        for t in people:
            # Count how many flowers have started by time t
            num_started = bisect_right(starts, t)
            # Count how many flowers have ended before t
            num_ended   = bisect_left(ends, t)
            # Those in bloom at t are started but not yet ended
            ans.append(num_started - num_ended)
        
        return ans
