class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # If k == 0, any nonempty subarray has OR >= 0
        if k == 0:
            return 1
        
        # bitâcounts in current window [L..R]
        count = [0] * 31
        OR_cur = 0
        best = float('inf')
        L = 0
        
        for R, v in enumerate(nums):
            # Add nums[R]
            for b in range(31):
                if (v >> b) & 1:
                    if count[b] == 0:
                        OR_cur |= (1 << b)
                    count[b] += 1
            
            # Try to shrink from left while OR_cur >= k
            while L <= R and OR_cur >= k:
                # Can we drop nums[L]?
                vL = nums[L]
                # simulate flipping off bits that would go to zero
                new_or = OR_cur
                for b in range(31):
                    if (vL >> b) & 1 and count[b] == 1:
                        new_or ^= (1 << b)
                if new_or >= k:
                    # actually drop it
                    for b in range(31):
                        if (vL >> b) & 1:
                            count[b] -= 1
                            if count[b] == 0:
                                OR_cur ^= (1 << b)
                    L += 1
                else:
                    break
            
            # After shrinking, if OR_cur >= k record length
            if OR_cur >= k:
                best = min(best, R - L + 1)
        
        return best if best != float('inf') else -1
