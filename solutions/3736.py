from collections import Counter

class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count total occurrences of each digit in s
        freq = Counter(s)
        
        # Scan adjacent pairs from left to right
        for i in range(len(s) - 1):
            d1, d2 = s[i], s[i+1]
            if d1 != d2:
                # Check if each digit's count equals its numeric value
                if freq[d1] == int(d1) and freq[d2] == int(d2):
                    return d1 + d2
        
        # No valid pair found
        return ""
