class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        # record positions of '1's
        ones = [i for i, ch in enumerate(s) if ch == '1']
        if len(ones) < k:
            return ""
        # find minimal window length over every k consecutive ones
        min_len = n + 1
        substrings = []
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            length = end - start + 1
            if length < min_len:
                min_len = length
                substrings = [s[start:end+1]]
            elif length == min_len:
                substrings.append(s[start:end+1])
        # return lexicographically smallest among them
        return min(substrings)
