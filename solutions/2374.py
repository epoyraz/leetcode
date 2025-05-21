class Solution:
    def totalSteps(self, nums):
        stack = []  # pairs of (value, steps_to_remove)
        ans = 0
        
        for x in nums:
            popped_max = 0
            popped_any = False
            
            # Pop all elements that are <= current, they will be "shielded" by x
            while stack and stack[-1][0] <= x:
                popped_any = True
                popped_max = max(popped_max, stack[-1][1])
                stack.pop()
            
            if not stack:
                # No larger to the left, this x never causes a removal chain
                steps = 0
            else:
                # There's a larger to the left, so x will be removed after popped_max+1 steps
                steps = popped_max + 1
            
            # Track the maximum steps over all elements
            ans = max(ans, steps)
            # Push current with its computed removal step count
            stack.append((x, steps))
        
        return ans
