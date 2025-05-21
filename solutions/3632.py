class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        prev_time = 0
        best_time = -1
        best_idx = float('inf')
        
        for idx, t in events:
            # time to press this button
            duration = t - prev_time
            # update best
            if duration > best_time or (duration == best_time and idx < best_idx):
                best_time = duration
                best_idx = idx
            prev_time = t
        
        return best_idx
