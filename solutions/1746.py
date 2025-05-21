class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        first = [-1] * 26
        max_len = -1
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            else:
                curr_len = i - first[idx] - 1
                if curr_len > max_len:
                    max_len = curr_len
        
        return max_len
