class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, delta):
        # add delta at index i (1-based)
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    def query(self, i):
        # sum from 1..i
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # 1) Coordinate-compress nums
        vals = sorted(set(nums))
        comp = {v:i+1 for i,v in enumerate(vals)}  # 1-based indices for Fenwick
        m = len(vals)
        
        # 2) Fenwicks to track counts in arr1 and arr2
        bit1 = FenwickTree(m)
        bit2 = FenwickTree(m)
        size1 = 0
        size2 = 0
        
        arr1 = []
        arr2 = []
        
        # 3) Process
        # first element -> arr1, second -> arr2
        # then from i=3..n apply rules
        # use 0-based indexing for Python lists but problem is 1-indexed
        # so nums[0] -> arr1, nums[1] -> arr2
        # then for idx from 2..n-1
        # 
        # helper to compute greaterCount in bitX of value v
        def greater_count(bit, sz, rank):
            # number strictly greater = total inserted sz minus count<=rank
            return sz - bit.query(rank)
        
        # place first
        r0 = comp[nums[0]]
        arr1.append(nums[0])
        bit1.update(r0, 1)
        size1 += 1
        
        # place second
        r1 = comp[nums[1]]
        arr2.append(nums[1])
        bit2.update(r1, 1)
        size2 += 1
        
        # remaining
        for x in nums[2:]:
            r = comp[x]
            g1 = greater_count(bit1, size1, r)
            g2 = greater_count(bit2, size2, r)
            if g1 > g2:
                # arr1
                arr1.append(x)
                bit1.update(r, 1)
                size1 += 1
            elif g1 < g2:
                arr2.append(x)
                bit2.update(r, 1)
                size2 += 1
            else:
                # tie on greaterCount -> choose smaller size
                if size1 <= size2:
                    arr1.append(x)
                    bit1.update(r, 1)
                    size1 += 1
                else:
                    arr2.append(x)
                    bit2.update(r, 1)
                    size2 += 1
        
        # concatenate
        return arr1 + arr2
