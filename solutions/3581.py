class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * 100  # since 0 <= nums[i] < n <= 100
        res = []
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                res.append(num)
                if len(res) == 2:
                    break
        return res
