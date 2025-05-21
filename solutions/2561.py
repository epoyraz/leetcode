class Solution:
    def distinctAverages(self, nums):
        nums.sort()
        i, j = 0, len(nums) - 1
        seen = set()
        while i < j:
            seen.add(nums[i] + nums[j])   # store sum, not the float average
            i += 1
            j -= 1
        return len(seen)
