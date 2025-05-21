class Solution:
    def maxLength(self, arr):
        def isUnique(s):
            return len(s) == len(set(s))

        def backtrack(index, current, max_len):
            if isUnique(current):
                max_len[0] = max(max_len[0], len(current))
            else:
                return
            for i in range(index, len(arr)):
                backtrack(i + 1, current + arr[i], max_len)

        max_len = [0]
        backtrack(0, "", max_len)
        return max_len[0]
