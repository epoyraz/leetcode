class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        # Helper to count number of pairs with distance <= mid
        def count_pairs(mid):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                # All indices in [left, right) form valid pairs with 'right'
                count += right - left
            return count
        
        # Binary search on distance
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
