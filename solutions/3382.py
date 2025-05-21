import bisect

class Solution(object):
    def numberOfSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 1) Next greater element index to the right (strictly greater)
        NG = [n] * n
        stack = []
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                NG[stack.pop()] = i
            stack.append(i)
        
        # 2) Group positions by value
        from collections import defaultdict
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        # 3) For each group, sum up counts
        ans = 0
        for v, plist in pos.items():
            # plist is sorted increasing by construction
            k = len(plist)
            for t, idx in enumerate(plist):
                # find first position in plist where plist[u] >= NG[idx]
                ub = bisect.bisect_left(plist, NG[idx])
                ans += (ub - t)
        
        return ans
