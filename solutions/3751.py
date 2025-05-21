class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Count how many kâs we already have
        orig_k = sum(1 for a in nums if a == k)
        
        best_gain = 0
        # Try aligning every other value v -> k by choosing x = k - v
        # The net change in #kâs when you shift a segment by x
        # is: (# of vâs in segment) - (# of kâs in segment).
        # We want the segment where that difference is maximized.
        for v in set(nums):
            if v == k:
                continue
            
            # Kadaneâs maximumâsubarray on weights w[i]:
            # w[i] = +1 if nums[i]==v, -1 if nums[i]==k, else 0
            curr = float('-inf')
            best_for_v = float('-inf')
            for a in nums:
                w = 1 if a == v else (-1 if a == k else 0)
                # either start new at w, or extend
                if curr < 0:
                    curr = w
                else:
                    curr += w
                best_for_v = max(best_for_v, curr)
            
            # only positive gain helps
            if best_for_v > 0:
                best_gain = max(best_gain, best_for_v)
        
        return orig_k + best_gain
