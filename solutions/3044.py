class Solution:
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        ops = 0
        n = len(nums)
        for i in range(n-1, -1, -1):
            ops += 1
            x = nums[i]
            # only 1..k matter
            if 1 <= x <= k and x not in seen:
                seen.add(x)
                if len(seen) == k:
                    return ops
        # problem guarantees we can collect 1..k
        return ops
