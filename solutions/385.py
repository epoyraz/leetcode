class Solution:
    def deserialize(self, s):
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = ''
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                if len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
            elif c == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:
                num += c
        return stack[0]
