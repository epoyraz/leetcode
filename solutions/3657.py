class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def can_split(intervals):
            m = len(intervals)
            if m < 3:
                return False
            # sort by start then end
            intervals.sort(key=lambda x: (x[0], x[1]))
            pre_max = [0] * (m + 1)
            for i in range(1, m + 1):
                pre_max[i] = max(pre_max[i-1], intervals[i-1][1])
            suf_min = [0] * (m + 1)
            suf_min[m] = float('inf')
            for i in range(m-1, -1, -1):
                suf_min[i] = min(suf_min[i+1], intervals[i][0])
            # count valid split positions
            count = 0
            for k in range(1, m):
                if pre_max[k] <= suf_min[k]:
                    count += 1
                    if count >= 2:
                        return True
            return False

        # extract x-intervals and y-intervals
        x_ints = [(x1, x2) for x1, y1, x2, y2 in rectangles]
        y_ints = [(y1, y2) for x1, y1, x2, y2 in rectangles]

        # check either horizontal or vertical
        return can_split(x_ints) or can_split(y_ints)
