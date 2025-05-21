class Solution:
    def minMaxGame(self, nums):
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums) // 2):
                a, b = nums[2*i], nums[2*i+1]
                if i % 2 == 0:
                    newNums.append(min(a, b))
                else:
                    newNums.append(max(a, b))
            nums = newNums
        return nums[0]
