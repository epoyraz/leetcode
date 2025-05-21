class Solution(object):
    def arrayNesting(self, nums):
        visited = [False] * len(nums)
        max_len = 0
        for i in range(len(nums)):
            if not visited[i]:
                count = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = nums[x]
                    count += 1
                if count > max_len:
                    max_len = count
        return max_len
