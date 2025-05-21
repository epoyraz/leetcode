class Solution(object):
    def constructArray(self, n, k):
        res = []
        left, right = 1, n
        while left <= right:
            if k > 1:
                if k % 2 == 1:
                    res.append(left)
                    left += 1
                else:
                    res.append(right)
                    right -= 1
                k -= 1
            else:
                res.append(left)
                left += 1
        return res
