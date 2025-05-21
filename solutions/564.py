class Solution(object):
    def nearestPalindromic(self, n):
        k = len(n)
        orig = int(n)
        candidates = set([
            str(10**(k-1) - 1),
            str(10**k + 1)
        ])
        prefix_len = (k + 1) // 2
        prefix = int(n[:prefix_len])
        for x in (prefix - 1, prefix, prefix + 1):
            if x < 0:
                continue
            s = str(x)
            # pad with leading zeros if needed
            if len(s) < prefix_len:
                s = s.zfill(prefix_len)
            # build palindrome
            if k % 2 == 0:
                pal = s + s[::-1]
            else:
                pal = s + s[:-1][::-1]
            candidates.add(pal)
        # remove original
        candidates.discard(n)

        ans = None
        min_diff = None
        for cand in candidates:
            # skip empty
            if not cand:
                continue
            val = int(cand)
            diff = abs(val - orig)
            if val == orig:
                continue
            if ans is None or diff < min_diff or (diff == min_diff and val < int(ans)):
                ans = cand
                min_diff = diff
        return ans
