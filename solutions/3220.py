class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested = 0    # number of devices we've tested so far (and hence total decrements applied to future devices)
        count = 0     # answer: how many devices get tested
        
        for b in batteryPercentages:
            # effective battery after all prior decrements is b - tested (floored at 0)
            if b > tested:
                count += 1
                tested += 1
        
        return count
