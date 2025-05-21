class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        # compute the slack segments g[0..n]:
        # g[0] = free time before first meeting,
        # g[i] = free time between meeting i-1 and i,
        # g[n] = free time after last meeting.
        g = [0] * (n + 1)
        g[0] = startTime[0]
        for i in range(1, n):
            g[i] = startTime[i] - endTime[i - 1]
        g[n] = eventTime - endTime[n - 1]

        # We can merge up to k+1 consecutive slack segments by moving k meetings:
        w = min(k + 1, n + 1)

        # sliding window of length w over g to find max sum
        curr = sum(g[:w])
        ans = curr
        for i in range(w, n + 1):
            curr += g[i] - g[i - w]
            if curr > ans:
                ans = curr

        return ans
