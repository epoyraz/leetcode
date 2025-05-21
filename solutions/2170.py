class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.max_or = 0
        self.count = 0

        def backtrack(index, current_or):
            if index == len(nums):
                if current_or == self.max_or:
                    self.count += 1
                return
            # Include nums[index]
            backtrack(index + 1, current_or | nums[index])
            # Exclude nums[index]
            backtrack(index + 1, current_or)

        # Compute the maximum OR
        for num in nums:
            self.max_or |= num

        backtrack(0, 0)
        return self.count
