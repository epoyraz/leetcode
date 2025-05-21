from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count frequencies of each character
        freq = Counter(s)
        # Build the first half of the palindrome
        half_chars = []
        mid_char = ''
        # Iterate characters in sorted order
        for ch in sorted(freq.keys()):
            count = freq[ch]
            # If odd count, reserve one for the middle
            if count % 2 == 1:
                mid_char = ch
            # Add count//2 copies to the half
            half_chars.append(ch * (count // 2))
        # Join to form the half string
        half = ''.join(half_chars)
        # Construct palindrome: half + middle + reverse(half)
        return half + mid_char + half[::-1]
