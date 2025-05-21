class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        n = len(s)
        half = n // 2
        
        # count vowels in first half
        count1 = sum(1 for c in s[:half] if c in vowels)
        # count vowels in second half
        count2 = sum(1 for c in s[half:] if c in vowels)
        
        return count1 == count2
