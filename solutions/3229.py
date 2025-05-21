class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        s = str(median)
        L = len(s)
        half = (L + 1)//2
        
        # Build up to 3 palindromes by mirroring prefix-1, prefix, prefix+1
        prefix = int(s[:half])
        cands = set()
        for d in (-1, 0, 1):
            p2 = prefix + d
            if p2 <= 0:
                continue
            t = str(p2)
            if L % 2 == 0:
                pal = int(t + t[::-1])
            else:
                pal = int(t + t[:-1][::-1])
            if 1 <= pal < 10**9:
                cands.add(pal)
        
        # Also consider the largest (L-1)-digit palindrome 999â¦9
        if L > 1:
            cands.add(int('9'*(L-1)))
        # And the smallest (L+1)-digit palindrome 1 0â¦0 1 (if still <1e9)
        if L < 9:
            cands.add(int('1' + '0'*(L-1) + '1'))
        
        best = float('inf')
        # Only O(5) candidates, each cost is O(n)
        for p in cands:
            cost = 0
            for x in nums:
                cost += abs(x - p)
            if cost < best:
                best = cost
        
        return best
