class Solution(object):
    def kthPalindrome(self, queries, intLength):
        res = []
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        max_count = 9 * start
        for q in queries:
            if q > max_count:
                res.append(-1)
            else:
                prefix = start + q - 1
                s = str(prefix)
                if intLength % 2 == 0:
                    pal = s + s[::-1]
                else:
                    pal = s + s[-2::-1]
                res.append(int(pal))
        return res
