import collections

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        cnt = collections.Counter(s)
        chars = [c for c in cnt if cnt[c] >= k]
        chars.sort(reverse=True)
        maxlen = len(s) // k

        def ok(seq):
            i = times = 0
            m = len(seq)
            for ch in s:
                if ch == seq[i]:
                    i += 1
                    if i == m:
                        times += 1
                        if times == k:
                            return True
                        i = 0
            return False

        res = ''
        cur = ['']
        for _ in xrange(maxlen):
            nxt = []
            for seq in cur:
                for ch in chars:
                    cand = seq + ch
                    if ok(cand):
                        nxt.append(cand)
            if not nxt:
                break
            res = nxt[0]
            cur = nxt
        return res
