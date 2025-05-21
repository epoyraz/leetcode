class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total = 0
        # sum_time is the sum of removal times in the current same-color group
        # max_time is the maximum removal time in that group
        sum_time = 0
        max_time = 0
        prev = None
        
        for c, t in zip(colors, neededTime):
            if c != prev:
                # finish previous group: remove all but the max
                total += sum_time - max_time
                # start new group
                sum_time = t
                max_time = t
                prev = c
            else:
                # continue the same-color group
                sum_time += t
                if t > max_time:
                    max_time = t
        
        # handle the last group
        total += sum_time - max_time
        return total
