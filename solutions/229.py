class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # First pass: find possible candidates
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Second pass: verify the candidates
        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > n // 3:
            result.append(candidate2)
        
        return result
