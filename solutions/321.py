class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def maxSubArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(a, b):
            res = []
            while a or b:
                if a > b:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res
        
        max_num = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            candidate = merge(maxSubArray(nums1, i), maxSubArray(nums2, k - i))
            max_num = max(max_num, candidate)
        
        return max_num
