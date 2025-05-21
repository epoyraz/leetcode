import bisect

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))  # remove duplicates and sort
        memo = {}

        def dp(i, prev):
            key = (i, prev)
            if key in memo:
                return memo[key]

            if i == len(arr1):
                return 0

            res = float('inf')

            # Option 1: Keep arr1[i] if it's strictly increasing
            if arr1[i] > prev:
                res = dp(i + 1, arr1[i])

            # Option 2: Replace with next greater in arr2
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                res = min(res, 1 + dp(i + 1, arr2[idx]))

            memo[key] = res
            return res

        ans = dp(0, -1)
        return ans if ans != float('inf') else -1
