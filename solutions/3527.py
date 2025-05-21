from bisect import bisect_left, bisect_right, insort

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+2)
    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx
    def pref(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s
    def suffix(self, idx):
        return self.pref(self.n) - self.pref(idx)

class Solution(object):
    def _insert_interval(self, L, R):
        self.start2end[L] = R
        self.end2start[R] = L
        insort(self.starts, L)
        length = R - L + 1
        self.ft_freq.add(length,  1)
        self.ft_sum .add(length, length+1)

    def _erase_interval(self, L, R):
        del self.start2end[L]
        del self.end2start[R]
        self.starts.pop(bisect_left(self.starts, L))
        length = R - L + 1
        self.ft_freq.add(length, -1)
        self.ft_sum .add(length, -(length+1))

    def numberOfAlternatingGroups(self, colors, queries):
        n = len(colors)
        # Build the diff array: 1 where colors[i] != colors[i+1]
        diff = [colors[i] ^ colors[(i+1) % n] for i in range(n)]

        # Build initial runs of consecutive 1's in diff (linear)
        self.start2end = {}
        self.end2start = {}
        self.starts     = []
        self.ft_freq    = Fenwick(n)   # freq of runs by length
        self.ft_sum     = Fenwick(n)   # sum of (length+1) by length

        i = 0
        while i < n:
            if diff[i] == 1:
                j = i
                while j+1 < n and diff[j+1] == 1:
                    j += 1
                self._insert_interval(i, j)
                i = j+1
            else:
                i += 1

        ans = []

        # Count windows of t consecutive 1's that *wrap* from n-1â0
        def cross_windows(t):
            if not (diff[0] and diff[-1]):
                return 0
            L = self.end2start[n-1]   # the run that ends at n-1
            R = self.start2end.get(0, -1)
            # If there is no run starting at 0, then start2end[0] is missing
            # => no wrap-wide run, but diff[0]==1 implies run MUST start at 0
            # so get(0,-1) is just a safety; in practice 0âstart2end if diff[0]==1.
            if L == 0:
                # single run covers entire array
                return 0 if n < t else (t-1)
            a = n - L       # length of tail segment
            b = R + 1       # length of head segment
            total = max(0, a + b - t + 1)
            inside = max(0, a - t + 1) + max(0, b - t + 1)
            return max(0, total - inside)

        # Flip diff[pos] to its new value, updating runs
        def flip(pos):
            old = diff[pos]
            new = colors[pos] ^ colors[(pos+1) % n]
            if old == new:
                return

            # 0â1: we may insert, extend left/right, but *never* merge across boundary
            if new == 1:
                # only consider linear neighbors:
                left_one  = (pos > 0     and diff[pos-1] == 1)
                right_one = (pos < n-1   and diff[pos+1] == 1)

                if not left_one and not right_one:
                    # brand new run [pos,pos]
                    self._insert_interval(pos, pos)

                elif left_one and not right_one:
                    # extend the existing run that ends at pos-1
                    L = self.end2start[pos-1]
                    R = self.start2end[L]
                    self._erase_interval(L, R)
                    self._insert_interval(L, R+1)

                elif not left_one and right_one:
                    # extend the existing run that starts at pos+1
                    R = self.start2end[pos+1]
                    L = self.end2start[R]
                    self._erase_interval(L, R)
                    self._insert_interval(pos, R)

                else:
                    # both sides linear: merge two runs
                    L1 = self.end2start[pos-1]
                    R1 = self.start2end[L1]
                    L2 = pos+1
                    R2 = self.start2end[L2]
                    self._erase_interval(L1, R1)
                    self._erase_interval(L2, R2)
                    self._insert_interval(L1, R2)

            # 1â0: we remove one cell from its run, possibly splitting
            else:
                idx_run = bisect_right(self.starts, pos) - 1
                L = self.starts[idx_run]
                R = self.start2end[L]
                self._erase_interval(L, R)

                if L == R == pos:
                    # run disappears entirely
                    pass
                elif L == pos:
                    # chop off left end
                    self._insert_interval(L+1, R)
                elif R == pos:
                    # chop off right end
                    self._insert_interval(L, R-1)
                else:
                    # split into two runs
                    self._insert_interval(L, pos-1)
                    self._insert_interval(pos+1, R)

            diff[pos] = new

        # Process each query
        for q in queries:
            if q[0] == 1:
                k = q[1]
                t = k - 1
                # windows fully inside one run:
                S0 = self.ft_freq.suffix(t-1)
                S1 = self.ft_sum .suffix(t-1)
                inside = S1 - t * S0
                # plus any that cross the end â start
                ans.append(inside + cross_windows(t))
            else:
                _, idx, col = q
                if colors[idx] != col:
                    # 1) update the tile color
                    colors[idx] = col
                    # 2) fix its two incident edges in diff
                    flip((idx-1) % n)
                    flip(idx)

        return ans
