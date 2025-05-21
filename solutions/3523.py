class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        # Build diff array: diff[i]=1 iff nums[i]-nums[i-1]==1
        diff = [0]*n
        for i in range(1, n):
            diff[i] = 1 if nums[i] - nums[i-1] == 1 else 0
        
        # Prefix sums of diff
        # ps[i] = sum of diff[0..i-1], so sum over diff[l..r] is ps[r+1] - ps[l]
        ps = [0]*(n+1)
        for i in range(n):
            ps[i+1] = ps[i] + diff[i]
        
        res = []
        for s in range(n - k + 1):
            e = s + k - 1
            # sum of diff[s+1..e] = ps[e+1] - ps[s+1]
            if ps[e+1] - ps[s+1] == k - 1:
                res.append(nums[e])
            else:
                res.append(-1)
        
        return res
