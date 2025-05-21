class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        mod = [0, 0, 0]
        for val in stones:
            mod[val % 3] += 1

        if mod[1] == 0 or mod[2] == 0:
            return mod[1] + mod[2] > 2 and mod[0] % 2 == 1
        return abs(mod[1] - mod[2]) > 2 or mod[0] % 2 == 0
