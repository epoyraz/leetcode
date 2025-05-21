class Solution(object):
    def smallestNumber(self, pattern):
        stack = []
        res = []
        num = 1

        for ch in pattern + 'I':
            stack.append(num)
            num += 1
            if ch == 'I':
                while stack:
                    res.append(str(stack.pop()))
        
        return ''.join(res)
