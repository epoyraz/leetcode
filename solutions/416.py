class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = set([0])
        
        for num in nums:
            next_dp = set()
            for t in dp:
                if t + num == target:
                    return True
                next_dp.add(t)
                next_dp.add(t + num)
            dp = next_dp
        
        return target in dp
