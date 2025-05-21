class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def moves(required_high_at_even):
            moves = 0
            for i in range(len(nums)):
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                right = nums[i + 1] if i + 1 < len(nums) else float('inf')
                if (required_high_at_even and i % 2 == 0) or (not required_high_at_even and i % 2 == 1):
                    continue
                min_adj = min(left, right)
                if nums[i] >= min_adj:
                    moves += nums[i] - (min_adj - 1)
            return moves
        
        return min(moves(True), moves(False))
