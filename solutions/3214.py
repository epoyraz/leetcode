class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def max_consecutive(bars):
            bars.sort()
            max_len = 1
            curr_len = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    curr_len += 1
                    max_len = max(max_len, curr_len)
                else:
                    curr_len = 1
            return max_len + 1  # +1 because consecutive gaps create N+1 cell span

        max_h = max_consecutive(hBars)
        max_v = max_consecutive(vBars)
        side = min(max_h, max_v)
        return side * side
