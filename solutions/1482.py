class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101  # frequency of each number from 0 to 100

        for num in nums:
            count[num] += 1

        # prefix sum to know how many numbers are smaller than current
        for i in range(1, 101):
            count[i] += count[i - 1]

        result = []
        for num in nums:
            result.append(count[num - 1] if num > 0 else 0)

        return result
