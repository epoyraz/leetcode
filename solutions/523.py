class Solution:
    def checkSubarraySum(self, nums, k):
        rem_map = {0: -1}
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            rem = total % k
            if rem in rem_map:
                if i - rem_map[rem] >= 2:
                    return True
            else:
                rem_map[rem] = i
        
        return False
