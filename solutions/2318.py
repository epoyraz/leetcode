class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        self.maxScore = 0
        self.best = [0] * 12

        def dfs(i, arrowsLeft, score, bob):
            if i == 12:
                if score > self.maxScore:
                    self.maxScore = score
                    self.best = bob[:]
                    self.best[0] += arrowsLeft  # put leftover arrows somewhere
                return

            # Option 1: Bob tries to win this section
            need = aliceArrows[i] + 1
            if arrowsLeft >= need:
                bob[i] = need
                dfs(i + 1, arrowsLeft - need, score + i, bob)
                bob[i] = 0  # backtrack

            # Option 2: Bob skips this section
            dfs(i + 1, arrowsLeft, score, bob)

        dfs(0, numArrows, 0, [0] * 12)
        return self.best
