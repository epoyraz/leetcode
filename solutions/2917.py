class Solution(object):
    def countPairs(self, nums, target):
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    cnt += 1
        return cnt
