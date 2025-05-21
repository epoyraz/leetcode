class Solution(object):
    def getMaxLen(self, nums):
        ans = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            start = i
            neg_count = 0
            first_neg = -1
            last_neg = -1
            while i < n and nums[i] != 0:
                if nums[i] < 0:
                    neg_count += 1
                    if first_neg == -1:
                        first_neg = i
                    last_neg = i
                i += 1
            end = i - 1
            if neg_count % 2 == 0:
                ans = max(ans, end - start + 1)
            else:
                ans = max(ans, end - first_neg, last_neg - start)
        return ans
