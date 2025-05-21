class Solution(object):
    def optimalDivision(self, nums):
        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return "%d/%d" % (nums[0], nums[1])
        rest = "/".join(str(x) for x in nums[1:])
        return "%d/(%s)" % (nums[0], rest)
