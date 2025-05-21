class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        best_score = -1
        best_div = None
        
        for d in divisors:
            score = 0
            for x in nums:
                if x % d == 0:
                    score += 1
            # Update if strictly better score, or same score but smaller divisor
            if score > best_score or (score == best_score and (best_div is None or d < best_div)):
                best_score = score
                best_div = d
        
        return best_div
