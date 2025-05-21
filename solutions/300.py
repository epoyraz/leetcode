class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
