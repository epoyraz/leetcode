class Solution:
    def findTheLongestBalancedSubstring(self, s):
        max_len = 0
        i = 0
        n = len(s)
        
        while i < n:
            zero_count = one_count = 0

            # Count consecutive zeros
            while i < n and s[i] == '0':
                zero_count += 1
                i += 1

            # Count consecutive ones
            while i < n and s[i] == '1':
                one_count += 1
                i += 1

            max_len = max(max_len, 2 * min(zero_count, one_count))

        return max_len
