from collections import Counter

class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        max_vowel = 0
        max_consonant = 0
        
        for ch, freq in cnt.items():
            if ch in vowels:
                max_vowel = max(max_vowel, freq)
            else:
                max_consonant = max(max_consonant, freq)
        
        return max_vowel + max_consonant
