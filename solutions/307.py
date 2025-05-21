class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def _sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._sum(right + 1) - self._sum(left)
