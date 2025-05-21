class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        bit = [0] * (n + 1)

        def add(i, v):
            while i <= n:
                bit[i] += v
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        for j in xrange(1, n - 2):
            add(nums[j - 1], 1)
            greater = 0
            for k in xrange(n - 1, j, -1):
                if nums[k] > nums[j]:
                    greater += 1
                elif nums[k] < nums[j]:
                    ans += query(nums[k] - 1) * greater
        return ans
