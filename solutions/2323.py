class Solution(object):
    def minBitFlips(self, start, goal):
        x = start ^ goal
        cnt = 0
        while x:
            x &= x - 1
            cnt += 1
        return cnt
