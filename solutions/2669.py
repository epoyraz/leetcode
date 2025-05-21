class Solution:
    def maximumCostSubstring(self, s, chars, vals):
        # Map character to custom value if it exists
        value_map = {c: v for c, v in zip(chars, vals)}
        
        def get_value(ch):
            return value_map.get(ch, ord(ch) - ord('a') + 1)
        
        max_sum = 0
        current = 0
        for ch in s:
            current += get_value(ch)
            if current < 0:
                current = 0
            max_sum = max(max_sum, current)
        
        return max_sum
