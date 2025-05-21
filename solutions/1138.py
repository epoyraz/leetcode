class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        base_satisfied = sum(c for c, g in zip(customers, grumpy) if g == 0)
        
        extra_satisfied = 0
        max_extra = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    extra_satisfied -= customers[i - minutes]
            max_extra = max(max_extra, extra_satisfied)
        
        return base_satisfied + max_extra
