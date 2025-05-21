class Solution:
    def maxScore(self, cardPoints, k):
        total = sum(cardPoints[:k])
        max_score = total
        n = len(cardPoints)

        for i in range(1, k + 1):
            total += cardPoints[-i] - cardPoints[k - i]
            max_score = max(max_score, total)

        return max_score
