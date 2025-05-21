class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        
        seen_digit = seen_dot = seen_exp = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif char in ['e', 'E']:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False
        
        return seen_digit
