class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Create a set from nums for O(1) lookups
        num_set = set(nums)
        max_length = 0
        
        # Check each number as a potential start of a sequence
        for num in num_set:
            # Only check sequences from their starting points
            # If num-1 exists, then num is not the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update max length if current sequence is longer
                max_length = max(max_length, current_length)
        
        return max_length