class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        result = []
        even_sum = sum(x for x in nums if x % 2 == 0)

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            result.append(even_sum)

        return result
