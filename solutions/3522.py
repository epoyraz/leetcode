class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            window = nums[i:i+k]
            good = True
            # Check strictly ascending by 1
            for j in range(1, k):
                if window[j] != window[j-1] + 1:
                    good = False
                    break
            if good:
                res.append(window[-1])
            else:
                res.append(-1)
        return res
