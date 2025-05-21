class Solution:
    def findMaxLength(self, nums):
        count = 0
        max_len = 0
        prefix_map = {0: -1}
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in prefix_map:
                max_len = max(max_len, i - prefix_map[count])
            else:
                prefix_map[count] = i
        
        return max_len
