class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                max_score = max(max_score, score)
            elif score > 0:
                # Sacrifice one score to gain power from the largest token
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score
