class Solution(object):
    def ambiguousCoordinates(self, s):
        def make(s):
            res = []
            if s == "0":
                res.append("0")
            elif s[0] == "0":
                if s[-1] != "0":
                    res.append(s[0] + "." + s[1:])
            elif s[-1] == "0":
                res.append(s)
            else:
                res.append(s)
                for i in range(1, len(s)):
                    res.append(s[:i] + "." + s[i:])
            return res
        
        s = s[1:-1]
        n = len(s)
        ans = []
        for i in range(1, n):
            left = make(s[:i])
            right = make(s[i:])
            for l in left:
                for r in right:
                    ans.append("(" + l + ", " + r + ")")
        return ans
