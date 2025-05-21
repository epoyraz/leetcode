class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_index[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        
        return ''.join(stack)
