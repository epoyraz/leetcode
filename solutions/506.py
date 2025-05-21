class Solution:
    def findRelativeRanks(self, score):
        sorted_score = sorted(enumerate(score), key=lambda x: -x[1])
        res = [""] * len(score)
        for i, (idx, _) in enumerate(sorted_score):
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)
        return res
