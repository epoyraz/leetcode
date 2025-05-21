class Solution(object):
    def makeSimilar(self, nums, target):
        ev_n, od_n = [], []
        ev_t, od_t = [], []
        for x in nums:
            (ev_n if x%2==0 else od_n).append(x)
        for x in target:
            (ev_t if x%2==0 else od_t).append(x)

        # They must have the same counts per parity (guaranteed possible)
        ev_n.sort()
        od_n.sort()
        ev_t.sort()
        od_t.sort()

        ops = 0
        # Sum positive shifts in the even list
        for a, b in zip(ev_n, ev_t):
            if b > a:
                ops += (b - a) // 2
        # Sum positive shifts in the odd list
        for a, b in zip(od_n, od_t):
            if b > a:
                ops += (b - a) // 2

        return ops
