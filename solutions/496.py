class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        return [next_greater.get(num, -1) for num in nums1]
