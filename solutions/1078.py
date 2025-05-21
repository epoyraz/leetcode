class Solution:
    def removeOuterParentheses(self, s):
        res = []
        balance = 0
        for ch in s:
            if ch == '(':
                if balance > 0:
                    res.append(ch)
                balance += 1
            else:  # ch == ')'
                balance -= 1
                if balance > 0:
                    res.append(ch)
        return ''.join(res)
