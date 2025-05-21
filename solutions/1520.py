class Solution(object):
    def numSteps(self, s):
        steps = 0
        carry = 0
        n = len(s)

        for i in range(n - 1, 0, -1):
            bit = int(s[i])
            if bit + carry == 1:
                carry = 1
                steps += 2  # add 1 and divide by 2
            else:
                steps += 1  # just divide by 2

        return steps + carry
