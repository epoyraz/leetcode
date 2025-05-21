class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        count = 0
        
        # k is the index of the largest side in the potential triangle
        for k in range(n-1, 1, -1):
            i, j = 0, k - 1
            # find all pairs (i, j) with nums[i] + nums[j] > nums[k]
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all elements from i to j-1 paired with j work
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
