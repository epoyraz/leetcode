class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def add(self, i, v):
        # add v at index i (0-based)
        i += 1
        while i <= self.n:
            self.fw[i] += v
            i += i & -i
    def sum(self, i):
        # sum[0..i] inclusive, i may be -1
        i += 1
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):
        if l > r: return 0
        return self.sum(r) - self.sum(l-1)

class Solution(object):
    def countOfPeaks(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # 1) build initial peak[] and Fenwick
        peak = [0]*n
        fw = Fenwick(n)
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peak[i] = 1
                fw.add(i, 1)

        ans = []
        for typ, x, y in queries:
            if typ == 1:
                l, r = x, y
                # peaks can only occur at i in [l+1..r-1]
                if r - l < 2:
                    ans.append(0)
                else:
                    ans.append(fw.range_sum(l+1, r-1))
            else:
                idx, val = x, y
                nums[idx] = val
                # recheck positions idx-1, idx, idx+1
                for i in (idx-1, idx, idx+1):
                    if 1 <= i < n-1:
                        newp = 1 if (nums[i] > nums[i-1] and nums[i] > nums[i+1]) else 0
                        if newp != peak[i]:
                            fw.add(i, newp - peak[i])
                            peak[i] = newp

        return ans
