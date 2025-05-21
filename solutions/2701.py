import bisect

class Solution(object):
    def minimumScore(self, s, t):
        n, m = len(s), len(t)
        # pre[i]: end position in s matching t[:i] as subsequence
        pre = [0] * (m + 1)
        pre[0] = -1
        j = 0
        for i in range(1, m + 1):
            # find t[i-1] after pre[i-1]
            while j < n and s[j] != t[i-1]:
                j += 1
            if j < n:
                pre[i] = j
                j += 1
            else:
                # no match
                pre[i] = float('inf')
        # if whole t matches, score = 0
        if pre[m] < float('inf'):
            return 0

        # suf[i]: start position in s matching t[i:] as subsequence
        suf = [0] * (m + 1)
        suf[m] = n
        j = n - 1
        for i in range(m - 1, -1, -1):
            # find t[i] before suf[i+1]
            while j >= 0 and s[j] != t[i]:
                j -= 1
            if j >= 0:
                suf[i] = j
                j -= 1
            else:
                suf[i] = -float('inf')

        # suf is strictly increasing with index i
        # find minimal (r - l + 1) == (idx - l), where idx = r+1
        ans = m  # worst: remove all
        for l in range(0, m + 1):
            if pre[l] == float('inf'):
                break
            # need suf[idx] > pre[l], idx in [l+1..m]
            idx = bisect.bisect_right(suf, pre[l])
            # ensure idx >= l+1
            if idx < l + 1:
                idx = l + 1
            if idx <= m:
                # removal segment [l, idx-1], length = idx - l
                ans = min(ans, idx - l)
        return ans
