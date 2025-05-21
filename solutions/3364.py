class Solution(object):
    def minimumValueSum(self, nums, andValues):
        """
        :type nums: List[int]
        :type andValues: List[int]
        :rtype: int
        """
        n, m = len(nums), len(andValues)
        INF = float('inf')
        # dp_prev[j]: min sum for first j elements split into (i-1) segments
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0
        # iterate over each segment i
        for i in range(1, m + 1):
            target = andValues[i - 1]
            dp_curr = [INF] * (n + 1)
            # prev_ands: list of tuples (and_val, best_prev_dp)
            prev_ands = []
            # build dp_curr by sweeping j
            for j in range(1, n + 1):
                x = nums[j - 1]
                # start new segment at j-1
                new_ands = [(x, dp_prev[j - 1])]
                # extend previous segments
                for (val, best_dp) in prev_ands:
                    new_val = val & x
                    # if merged with last AND in new_ands
                    if new_ands[-1][0] == new_val:
                        # keep minimal dp from possible starts
                        new_ands[-1] = (new_val, min(new_ands[-1][1], best_dp))
                    else:
                        new_ands.append((new_val, best_dp))
                # if target present as AND, update dp_curr[j]
                for (val, best_dp) in new_ands:
                    if val == target and best_dp != INF:
                        # segment value is nums[j-1]
                        dp_curr[j] = best_dp + nums[j - 1]
                        break  # only one target entry in new_ands
                # prepare for next j
                prev_ands = new_ands
            dp_prev = dp_curr
        res = dp_prev[n]
        return res if res < INF else -1

# Example usage:
# sol = Solution()
# print(sol.minimumValueSum([1,4,3,3,2], [0,3,3,2]))  # 12
# print(sol.minimumValueSum([2,3,5,7,7,7,5], [0,7,5]))  # 17
# print(sol.minimumValueSum([1,2,3,4], [2]))           # -1