class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # dp_set holds all distinct ORâvalues of subarrays ending at the previous index
        dp_set = set()
        ans = float('inf')
        
        for num in nums:
            # Build the new set of ORâvalues for subarrays ending here:
            # either start at this num, or extend each previous subarray by ORâing with num
            new_set = {num}
            for prev_or in dp_set:
                new_set.add(prev_or | num)
            
            # Check each ORâvalueâs distance to k
            for val in new_set:
                diff = abs(k - val)
                if diff < ans:
                    ans = diff
                    # early exit if we hit zero
                    if ans == 0:
                        return 0
            
            # Move forward
            dp_set = new_set
        
        return ans
