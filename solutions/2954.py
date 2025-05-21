from collections import defaultdict

class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = defaultdict(int)
        distinct = 0
        window_sum = 0
        max_sum = 0

        # initialize first window [0..k-1]
        for i in range(k):
            x = nums[i]
            window_sum += x
            if freq[x] == 0:
                distinct += 1
            freq[x] += 1

        if distinct >= m:
            max_sum = window_sum

        # slide window
        for i in range(k, n):
            # remove nums[i-k]
            y = nums[i - k]
            freq[y] -= 1
            if freq[y] == 0:
                distinct -= 1
                del freq[y]
            window_sum -= y

            # add nums[i]
            x = nums[i]
            if freq[x] == 0:
                distinct += 1
            freq[x] += 1
            window_sum += x

            # check
            if distinct >= m and window_sum > max_sum:
                max_sum = window_sum

        return max_sum
