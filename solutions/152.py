class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            candidates = (num, num * max_prod, num * min_prod)
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)
        
        return result
