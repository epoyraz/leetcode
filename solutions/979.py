class Solution:
    def diStringMatch(self, s):
        low, high = 0, len(s)
        res = []

        for char in s:
            if char == 'I':
                res.append(low)
                low += 1
            else:  # char == 'D'
                res.append(high)
                high -= 1

        res.append(low)  # low == high at the end
        return res
