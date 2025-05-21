class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for start, end in zip(l, r):
            sub = nums[start:end+1]
            sub.sort()
            diff = sub[1] - sub[0]
            ok = True
            for i in range(2, len(sub)):
                if sub[i] - sub[i-1] != diff:
                    ok = False
                    break
            res.append(ok)
        return res
