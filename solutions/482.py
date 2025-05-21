class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '').upper()
        n = len(s)
        first = n % k or k
        parts = [s[:first]]
        for i in range(first, n, k):
            parts.append(s[i:i + k])
        return '-'.join(parts)
