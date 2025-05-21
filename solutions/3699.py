import bisect

class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        # ratio_map[(a',b')] = {'L': [q1, q2, ...], 'R': [r1, r2, ...]}
        ratio_map = {}

        # Build left-pairs (p, q) with q - p > 1
        for p in range(n - 2):
            ap = nums[p]
            for q in range(p + 2, n):
                bq = nums[q]
                g = gcd(ap, bq)
                key = (ap // g, bq // g)
                ratio_map.setdefault(key, {'L': [], 'R': []})['L'].append(q)

        # Build right-pairs (r, s) with s - r > 1
        for r in range(2, n - 1):
            br = nums[r]
            for s in range(r + 2, n):
                as_ = nums[s]
                g = gcd(as_, br)
                key = (as_ // g, br // g)
                ratio_map.setdefault(key, {'L': [], 'R': []})['R'].append(r)

        total = 0
        # For each ratio bucket, count valid (p,q,r,s) with r >= q+2
        for bucket in ratio_map.values():
            Lq = bucket['L']
            Rr = bucket['R']
            if not Lq or not Rr:
                continue
            Lq.sort()
            Rr.sort()
            m = len(Rr)
            for q in Lq:
                # find first r >= q + 2
                idx = bisect.bisect_left(Rr, q + 2)
                total += (m - idx)

        return total
