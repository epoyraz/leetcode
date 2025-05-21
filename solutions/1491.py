class Solution(object):
    def numTimesAllBlue(self, flips):
        res = 0
        max_flip = 0

        for i, flip in enumerate(flips, 1):
            max_flip = max(max_flip, flip)
            if max_flip == i:
                res += 1

        return res
