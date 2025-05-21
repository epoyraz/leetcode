class Solution(object):
    def countHillValley(self, nums):
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
            l = i - 1
            while l >= 0 and nums[l] == nums[i]:
                l -= 1
            r = i + 1
            while r < n and nums[r] == nums[i]:
                r += 1
            if l >= 0 and r < n:
                if nums[i] > nums[l] and nums[i] > nums[r]:
                    ans += 1
                elif nums[i] < nums[l] and nums[i] < nums[r]:
                    ans += 1
        return ans
