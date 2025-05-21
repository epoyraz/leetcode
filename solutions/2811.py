class Solution(object):
    def minimumSum(self, n, k):
        used = set()
        res = 0
        i = 1
        while len(used) < n:
            if k - i not in used:
                used.add(i)
                res += i
            i += 1
        return res
