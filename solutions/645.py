class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        num_set = set()
        duplicate = -1
        total = 0
        
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)
            total += num
        
        missing = (n * (n + 1)) // 2 - (total - duplicate)
        return [duplicate, missing]
