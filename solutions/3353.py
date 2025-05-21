class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2:
            return False
        
        rev = s[::-1]
        seen = set(rev[i:i+2] for i in range(n-1))
        
        for i in range(n-1):
            if s[i:i+2] in seen:
                return True
        
        return False
