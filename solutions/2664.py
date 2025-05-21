class Solution(object):
    def maximizeGreatness(self, nums):
        # Sort the original values
        A = sorted(nums)
        B = A[:]  # multiset for perm
        
        count = 0
        j = 0  # pointer into A
        
        # Greedily match each b in B to the smallest A[j] it can beat
        for b in B:
            if j < len(A) and b > A[j]:
                count += 1
                j += 1
        
        return count
