class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        diffs = [(a + b, i) for i, (a, b) in enumerate(zip(aliceValues, bobValues))]
        diffs.sort(reverse=True)
        scoreA = scoreB = 0
        for turn, (_, i) in enumerate(diffs):
            if turn % 2 == 0:
                scoreA += aliceValues[i]
            else:
                scoreB += bobValues[i]
        if scoreA > scoreB:
            return 1
        if scoreA < scoreB:
            return -1
        return 0
