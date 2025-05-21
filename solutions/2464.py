class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        zeros = 0
        max_time = 0

        for c in s:
            if c == '0':
                zeros += 1
            elif zeros > 0:
                max_time = max(max_time + 1, zeros)

        return max_time
