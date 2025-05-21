class Solution:
    def subsetXORSum(self, nums):
        self.total = 0
        def dfs(i, xor):
            if i == len(nums):
                self.total += xor
                return
            dfs(i + 1, xor ^ nums[i])
            dfs(i + 1, xor)
        dfs(0, 0)
        return self.total
