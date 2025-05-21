from bisect import bisect_right

class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        dp = []
        ans = []
        for x in obstacles:
            # find length of longest non-decreasing subsequence ending here
            pos = bisect_right(dp, x)
            if pos == len(dp):
                dp.append(x)
            else:
                dp[pos] = x
            ans.append(pos + 1)
        return ans
