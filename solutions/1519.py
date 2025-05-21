class Solution(object):
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        total = sum(nums)
        curr_sum = 0
        result = []
        for num in nums:
            curr_sum += num
            result.append(num)
            if curr_sum > total - curr_sum:
                break
        return result
