class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        start = 0  # Current position in nums

        for group in groups:
            found = False
            while start + len(group) <= len(nums):
                # Check if the current slice matches the group
                if nums[start:start+len(group)] == group:
                    # Move start past the matched group to ensure disjoint
                    start += len(group)
                    found = True
                    break
                start += 1
            if not found:
                return False

        return True
