from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        max_deque = deque()  # To keep track of maximum elements in the current window
        min_deque = deque()  # To keep track of minimum elements in the current window
        
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Maintain the max deque (elements in decreasing order)
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain the min deque (elements in increasing order)
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Ensure that the difference between max and min is within the limit
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements outside the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the max length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length
