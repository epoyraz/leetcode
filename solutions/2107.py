class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        res = []
        for i, s in enumerate(nums):
            # flip the i-th bit of the i-th string
            res.append('0' if s[i] == '1' else '1')
        return ''.join(res)
