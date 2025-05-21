class Solution:
    def addToArrayForm(self, num, k):
        res = []
        i = len(num) - 1
        carry = k

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
            res.append(carry % 10)
            carry //= 10
            i -= 1

        return res[::-1]
