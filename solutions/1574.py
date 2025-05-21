class Solution(object):
    def maxProduct(self, nums):
        # Find the two largest numbers in one pass
        max1 = max2 = 0
        for x in nums:
            if x > max1:
                max2, max1 = max1, x
            elif x > max2:
                max2 = x
        return (max1 - 1) * (max2 - 1)
