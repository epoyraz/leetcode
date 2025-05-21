class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1) Count total occurrences of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        # 2) Find the maximum number of rounds = max frequency
        M = max(freq)

        # 3) Collect exactly the M-th occurrence of each char whose total freq == M
        seen = [0] * 26
        res = []
        for ch in s:
            ci = ord(ch) - 97
            seen[ci] += 1
            # If this char appears M times total, and this is its M-th occurrence,
            # it survives until just before the last removal.
            if freq[ci] == M and seen[ci] == M:
                res.append(ch)

        # The order in `res` matches their order in s, which is the string
        # just before the final operation.
        return "".join(res)
