class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n+1)
    def update(self, i, v):
        # add v at index i (1-based)
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def query(self, i):
        # sum from 1..i
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

class Solution(object):
    def findMinimumTime(self, tasks):
        # tasks: List of [start, end, duration]
        # times go 1..2000
        # 1) sort by end-time
        tasks.sort(key=lambda x: x[1])
        maxT = max(end for _, end, _ in tasks)
        bit = Fenwick(maxT)
        selected = [0] * (maxT + 1)  # 1-based times

        for start, end, dur in tasks:
            # how many already selected in [start..end]
            have = bit.range_query(start, end)
            need = dur - have
            t = end
            # pick 'need' new points from the right end backwards
            while need > 0:
                if selected[t] == 0:
                    selected[t] = 1
                    bit.update(t, 1)
                    need -= 1
                t -= 1

        # total seconds on = total selected points
        return sum(selected)
