class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        # Add delay and wrap around 24-hour clock
        return (arrivalTime + delayedTime) % 24
