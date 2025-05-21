class Solution:
    def rearrangeCharacters(self, s, target):
        # Count frequencies in s
        freq_s = {}
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        
        # Count frequencies in target
        freq_t = {}
        for ch in target:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        
        # For each character in target, compute how many copies s supports
        # The answer is the minimum over these quotas.
        copies = float('inf')
        for ch, needed in freq_t.items():
            copies = min(copies, freq_s.get(ch, 0) // needed)
        
        return copies if copies != float('inf') else 0
