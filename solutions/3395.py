class Solution(object):
    def minAnagramLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        n = len(s)
        total = Counter(s)

        # helper: all divisors of n, in ascending order
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i * i != n:
                    divs.append(n // i)
            i += 1
        divs.sort()

        # try each possible block-size k
        for k in divs:
            B = n // k  # number of blocks
            # quick check: each char count must be divisible by B
            ok = True
            per = {}
            for ch, cnt in total.items():
                if cnt % B:
                    ok = False
                    break
                per[ch] = cnt // B
            if not ok:
                continue

            # now verify every length-k block matches per[]
            from collections import Counter
            valid = True
            for start in range(0, n, k):
                blk = s[start:start+k]
                if Counter(blk) != per:
                    valid = False
                    break
            if valid:
                return k

        # (theoretically won't happen, since k = n always works)
        return n
