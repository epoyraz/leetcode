class Solution:
    def digitCount(self, num):
        freq = {}
        for ch in num:
            freq[ch] = freq.get(ch, 0) + 1
        
        for i, ch in enumerate(num):
            if freq.get(str(i), 0) != int(ch):
                return False
        return True
