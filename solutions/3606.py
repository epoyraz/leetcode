class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        return min(digit_sum(num) for num in nums)
