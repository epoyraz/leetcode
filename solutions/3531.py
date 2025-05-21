import functools

class Solution(object):
    def minDamage(self, power, damage, health):
        # build (weight, processing) pairs
        jobs = []
        for w, h in zip(damage, health):
            t = (h + power - 1) // power
            jobs.append((w, t))

        # sort by decreasing w/t ratio
        def cmp(a, b):
            w1, t1 = a
            w2, t2 = b
            # want w1/t1 > w2/t2 => w1*t2 > w2*t1
            if w1 * t2 > w2 * t1:
                return -1
            if w1 * t2 < w2 * t1:
                return 1
            return 0

        jobs.sort(key=functools.cmp_to_key(cmp))

        # accumulate completion time and weighted sum
        total_damage = 0
        elapsed = 0
        for w, t in jobs:
            elapsed += t
            total_damage += w * elapsed

        return total_damage
