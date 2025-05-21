class Solution:
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')
        for n in reversed(nums):
            if n < third:
                return True
            while stack and n > stack[-1]:
                third = stack.pop()
            stack.append(n)
        return False
