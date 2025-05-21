class Solution(object):
    def splitPainting(self, segments):
        # Build sweep-line events: +color at start, -color at end
        events = []
        for start, end, color in segments:
            events.append((start, color))
            events.append((end, -color))
        # Sort by position
        events.sort()
        
        res = []
        curr_sum = 0
        prev_pos = None
        i = 0
        n = len(events)
        
        # Sweep through events
        while i < n:
            pos = events[i][0]
            # Before processing events at pos, record segment from prev_pos to pos
            if prev_pos is not None and prev_pos < pos and curr_sum > 0:
                res.append([prev_pos, pos, curr_sum])
            # Process all events at this position
            while i < n and events[i][0] == pos:
                _, delta = events[i]
                curr_sum += delta
                i += 1
            prev_pos = pos
        
        return res
