class Solution(object):
    def findTheLongestSubstring(self, s):
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state = 0
        max_len = 0
        seen = {0: -1}  # bitmask -> first index

        for i, ch in enumerate(s):
            if ch in vowel_to_bit:
                # Flip the corresponding bit using XOR
                state ^= (1 << vowel_to_bit[ch])
            if state in seen:
                max_len = max(max_len, i - seen[state])
            else:
                seen[state] = i

        return max_len
