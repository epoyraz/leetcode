class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        from collections import defaultdict
        
        def digit_sum(num):
            return sum(int(d) for d in str(num))
        
        box_counts = defaultdict(int)
        
        for ball in range(lowLimit, highLimit + 1):
            box = digit_sum(ball)
            box_counts[box] += 1
        
        return max(box_counts.values())
