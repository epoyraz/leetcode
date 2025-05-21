class Solution:
    def canBeValid(self, s, locked):
        n = len(s)
        if n % 2 != 0:
            return False

        # Left to right check
        balance = 0  # represents net open brackets
        flex = 0     # number of unlocked positions
        for i in range(n):
            if locked[i] == '1':
                balance += 1 if s[i] == '(' else -1
            else:
                flex += 1

            if balance + flex < 0:
                return False

        # Right to left check
        balance = 0
        flex = 0
        for i in reversed(range(n)):
            if locked[i] == '1':
                balance += 1 if s[i] == ')' else -1
            else:
                flex += 1

            if balance + flex < 0:
                return False

        return True
