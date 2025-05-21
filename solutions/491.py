class Solution:
    def findSubsequences(self, nums):
        ans = []

        def dfs(idx, path):
            if len(path) >= 2:          # record any subsequence of length â¥ 2
                ans.append(path[:])     # append a copy
            if idx == len(nums):
                return

            used = set()                # values tried at *this* depth
            for i in range(idx, len(nums)):
                if nums[i] in used:     # skip duplicates on this level
                    continue
                if not path or nums[i] >= path[-1]:   # keep non-decreasing
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1, path)    # explore further
                    path.pop()          # back-track

        dfs(0, [])
        return ans
