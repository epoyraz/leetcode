import bisect

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr:    List[int]
        :rtype: int
        """
        # Map each value in target to its index
        pos = {val: i for i, val in enumerate(target)}
        
        # Build the sequence of target-indices for elements in arr that appear in target
        seq = [pos[x] for x in arr if x in pos]
        
        # Find length of Longest Increasing Subsequence in seq
        tails = []
        for x in seq:
            # Find insertion point for x in tails to keep it strictly increasing
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        
        # We need to insert the missing elements of target
        return len(target) - len(tails)
