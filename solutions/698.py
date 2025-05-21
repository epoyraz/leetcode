class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        n = len(nums)
        nums.sort(reverse=True)
        memo = {}
        
        def dfs(used, curr_sum):
            if used in memo:
                return memo[used]
            if used == (1 << n) - 1:
                return True
            for i in range(n):
                if not (used >> i) & 1:
                    if curr_sum + nums[i] > target:
                        continue
                    if dfs(used | (1 << i), (curr_sum + nums[i]) % target):
                        memo[used] = True
                        return True
            memo[used] = False
            return False
        
        return dfs(0, 0)
