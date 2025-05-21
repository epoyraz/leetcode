class Solution:
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Find positions of min and max
        min_i = max_i = 0
        for idx, val in enumerate(nums):
            if val < nums[min_i]:
                min_i = idx
            if val > nums[max_i]:
                max_i = idx
        
        # Let i be the earlier index, j the later
        i, j = min(min_i, max_i), max(min_i, max_i)
        
        # 1) Remove both from front: need j+1 deletions
        ops_front = j + 1
        # 2) Remove both from back: need n - i deletions
        ops_back = n - i
        # 3) Remove one from front (i) and one from back (j)
        ops_mix1 = (i + 1) + (n - j)
        # (The other mixed ordering is always worse, since j>=i)
        
        return min(ops_front, ops_back, ops_mix1)
