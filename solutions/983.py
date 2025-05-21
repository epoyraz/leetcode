class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0  # pointer for popped
        
        for x in pushed:
            stack.append(x)
            # pop while top matches the next in popped
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        # If we've matched all popped elements, it's valid
        return j == len(popped)
