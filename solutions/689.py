class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        sum_k = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        sum_k[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            sum_k[i] = curr_sum

        left = [0] * len(sum_k)
        best = 0
        for i in range(len(sum_k)):
            if sum_k[i] > sum_k[best]:
                best = i
            left[i] = best

        right = [0] * len(sum_k)
        best = len(sum_k) - 1
        for i in range(len(sum_k) - 1, -1, -1):
            if sum_k[i] >= sum_k[best]:
                best = i
            right[i] = best

        res = None
        max_total = 0
        for j in range(k, len(sum_k) - k):
            i, l = left[j - k], right[j + k]
            total = sum_k[i] + sum_k[j] + sum_k[l]
            if res is None or total > max_total:
                max_total = total
                res = [i, j, l]
        
        return res
