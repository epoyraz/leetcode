class Solution:
    def countAsterisks(self, s):
        in_bar = False
        count = 0
        for ch in s:
            if ch == '|':
                in_bar = not in_bar
            elif ch == '*' and not in_bar:
                count += 1
        return count
