import bisect
from collections import defaultdict

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        n = length // 2
        A, B = nums[:n], nums[n:]
        
        # Collect all subset-sums of A and B by how many elements they use
        sumsA = defaultdict(list)
        sumsB = defaultdict(list)
        
        def dfsA(i, cnt, s):
            if i == n:
                sumsA[cnt].append(s)
                return
            dfsA(i+1, cnt, s)            # skip A[i]
            dfsA(i+1, cnt+1, s + A[i])   # take A[i]
        
        def dfsB(i, cnt, s):
            if i == n:
                sumsB[cnt].append(s)
                return
            dfsB(i+1, cnt, s)            # skip B[i]
            dfsB(i+1, cnt+1, s + B[i])   # take B[i]
        
        dfsA(0, 0, 0)
        dfsB(0, 0, 0)
        
        # Sort the lists for B so we can binary-search them
        for cnt in sumsB:
            sumsB[cnt].sort()
        
        total = sum(nums)
        half = total / 2.0
        best = float('inf')
        
        # Try picking k elements from A and (n-k) from B
        for cntA, listA in sumsA.iteritems():
            cntB = n - cntA
            if cntB not in sumsB:
                continue
            listB = sumsB[cntB]
            for sA in listA:
                # We want sA + sB as close to total/2 as possible
                target = half - sA
                idx = bisect.bisect_left(listB, target)
                # Check the candidate at idx
                if idx < len(listB):
                    sB = listB[idx]
                    diff = abs(2 * (sA + sB) - total)
                    if diff < best:
                        best = diff
                # And also check the one just before
                if idx > 0:
                    sB = listB[idx - 1]
                    diff = abs(2 * (sA + sB) - total)
                    if diff < best:
                        best = diff
        
        return int(best)
