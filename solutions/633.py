class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(c**0.5)
        while left <= right:
            curr = left * left + right * right
            if curr == c:
                return True
            elif curr < c:
                left += 1
            else:
                right -= 1
        return False
