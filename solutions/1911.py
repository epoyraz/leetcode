class Solution(object):
    def minElements(self, nums, limit, goal):
        diff = abs(goal - sum(nums))
        return (diff + limit - 1) // limit
