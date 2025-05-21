class Fenwick:
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def update(self, i, v):
        i += 1
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i
        
        arr = [pos2[v] for v in nums1]
        
        leftBIT = Fenwick(n)
        left = [0] * n
        for i in range(n):
            left[i] = leftBIT.query(arr[i] - 1)
            leftBIT.update(arr[i], 1)
        
        rightBIT = Fenwick(n)
        right = [0] * n
        for i in range(n - 1, -1, -1):
            right[i] = rightBIT.query(n - 1) - rightBIT.query(arr[i])
            rightBIT.update(arr[i], 1)
        
        return sum(l * r for l, r in zip(left, right))
