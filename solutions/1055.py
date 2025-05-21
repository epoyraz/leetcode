class Solution:
    def numPairsDivisibleBy60(self, time):
        count = [0] * 60
        res = 0
        for t in time:
            r = t % 60
            c = (60 - r) % 60
            res += count[c]
            count[r] += 1
        return res
