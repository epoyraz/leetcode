class Solution(object):
    def hasSpecialSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        for i in range(n - k + 1):
            # Candidate window s[i:i+k]
            c = s[i]
            # 1) all k chars are c?
            if any(s[j] != c for j in range(i, i + k)):
                continue
            # 2) boundary checks
            if i > 0 and s[i - 1] == c:
                continue
            if i + k < n and s[i + k] == c:
                continue
            # found a valid special substring
            return True
        return False
