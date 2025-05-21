class Solution:
    def createSortedArray(self, instructions):
        MOD = 10**9 + 7
        # Coordinate maximum
        M = max(instructions)
        # Fenwick tree for frequencies, size M+1 (1-indexed)
        bit = [0] * (M + 2)
        
        def update(i, v):
            while i <= M+1:
                bit[i] += v
                i += i & -i
        
        def query(i):
            # sum from 1..i
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        
        cost = 0
        total = 0  # total elements inserted so far
        
        for x in instructions:
            # map x to index x+1 in BIT to avoid zero
            idx = x + 1
            less = query(idx - 1)
            greater = total - query(idx)
            cost += min(less, greater)
            cost %= MOD
            
            # insert x
            update(idx, 1)
            total += 1
        
        return cost
