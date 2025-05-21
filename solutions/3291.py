class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def popcount(x):
            return bin(x).count('1')
        
        n = len(nums)
        if n <= 1:
            return True
        
        # 1) identify runs of equal popcount
        runs = []
        start = 0
        for i in range(n-1):
            if popcount(nums[i]) != popcount(nums[i+1]):
                runs.append((start, i))
                start = i+1
        runs.append((start, n-1))
        
        # 2) sort each run in-place
        arr = list(nums)
        for l, r in runs:
            arr[l:r+1] = sorted(arr[l:r+1])
        
        # 3) check if fully sorted
        return all(arr[i] <= arr[i+1] for i in range(n-1))
