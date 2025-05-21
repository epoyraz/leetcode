class Solution:
    def shortestSequence(self, rolls, k):
        seen = [False] * (k + 1)
        seen_count = 0
        rounds = 0
        
        for x in rolls:
            if not seen[x]:
                seen[x] = True
                seen_count += 1
                if seen_count == k:
                    rounds += 1
                    # reset for next round
                    seen = [False] * (k + 1)
                    seen_count = 0
        
        # The shortest missing subsequence length is the number of complete
        # rounds we can form plus one.
        return rounds + 1
