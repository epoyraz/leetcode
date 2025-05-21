class Solution:
    def rearrangeArray(self, nums):
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        result = []
        for i in range(len(nums) // 2):
            result.append(pos[i])
            result.append(neg[i])
        return result
