import bisect

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def find_kth(self, k):
        # smallest i such that prefix sum >= k
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            t = idx + bit_mask
            if t <= self.n and self.fw[t] < k:
                idx = t
                k -= self.fw[t]
            bit_mask >>= 1
        return idx + 1

class Solution(object):
    def closestRoom(self, rooms, queries):
        # sort rooms by size descending
        rooms.sort(key=lambda x: -x[1])
        # augment queries with original index and sort by minSize descending
        qs = []
        for i, (pref, ms) in enumerate(queries):
            qs.append((ms, pref, i))
        qs.sort(key=lambda x: -x[0])

        # compress room IDs
        ids = [r[0] for r in rooms]
        ids.sort()
        # Fenwick on positions of ids
        m = len(ids)
        fw = Fenwick(m)

        ans = [-1] * len(queries)
        ridx = 0  # pointer in rooms
        for ms, pref, qi in qs:
            # add all rooms with size >= ms
            while ridx < len(rooms) and rooms[ridx][1] >= ms:
                rid = rooms[ridx][0]
                pos = bisect.bisect_left(ids, rid) + 1
                fw.update(pos, 1)
                ridx += 1

            if fw.query(m) == 0:
                ans[qi] = -1
                continue

            # find predecessor <= pref
            ip = bisect.bisect_right(ids, pref)  # count <= pref
            if ip > 0:
                cnt = fw.query(ip)
                if cnt > 0:
                    p_pos = fw.find_kth(cnt)
                    pred = ids[p_pos - 1]
                else:
                    pred = None
            else:
                pred = None

            # find successor > pref
            total = fw.query(m)
            cntp = fw.query(ip)
            if total > cntp:
                s_pos = fw.find_kth(cntp + 1)
                succ = ids[s_pos - 1]
            else:
                succ = None

            # choose closest
            best = -1
            best_diff = 10**20
            for cand in (pred, succ):
                if cand is not None:
                    d = abs(cand - pref)
                    if d < best_diff or (d == best_diff and cand < best):
                        best = cand
                        best_diff = d
            ans[qi] = best
        return ans
