class Solution:
    def longestSubsequence(self, s, k):
        value = 0       # numeric value of currently chosen bits
        length = 0      # how many bits chosen so far
        ans = 0         # length of subsequence

        for ch in reversed(s):          # scan from right-most to left
            if ch == '0':
                # always safe to prepend a 0
                length += 1
                ans += 1
            else:                       # ch == '1'
                bit_val = 1 << length   # weight of this '1' if we prepend it
                if value + bit_val <= k:
                    value += bit_val
                    length += 1
                    ans += 1
                # else we skip this '1'

        return ans
