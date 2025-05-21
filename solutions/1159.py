class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {ch: i for i, ch in enumerate(s)}
        stack = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and ch < stack[-1] and i < last_index[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)
