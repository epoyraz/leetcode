class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        events = []
        total_area = 0
        for x, y, l in squares:
            # each square contributes slope +l starting at y,
            # and slope âl starting at y+l
            events.append((y, l))
            events.append((y + l, -l))
            total_area += l * l

        half = total_area / 2.0

        # sort by yâcoordinate
        events.sort(key=lambda ev: ev[0])

        curr_slope = 0         # current d/dh of areaâbelow
        curr_f = 0.0           # areaâbelow at prev_y
        prev_y = events[0][0]  # start sweeping from the first event

        i = 0
        n_ev = len(events)
        while i < n_ev:
            y = events[i][0]

            # between prev_y and y, areaâbelow grows linearly with slope
            if y > prev_y:
                if curr_slope != 0:
                    f_at_y = curr_f + curr_slope * (y - prev_y)
                    # check if halfâarea lies in [curr_f, f_at_y]
                    if curr_f <= half <= f_at_y:
                        # solve curr_f + curr_slope*(h - prev_y) = half
                        return prev_y + (half - curr_f) / curr_slope
                    curr_f = f_at_y
                else:
                    # slope zero â f constant; if it's exactly half, return prev_y
                    if curr_f == half:
                        return float(prev_y)
                    # otherwise nothing changes

            # now process all events at y
            delta = 0
            while i < n_ev and events[i][0] == y:
                delta += events[i][1]
                i += 1
            curr_slope += delta
            prev_y = y

        # after all events, slope must be zero and curr_f == total_area
        # half <= curr_f always holds; the minimal y is prev_y
        return float(prev_y)
