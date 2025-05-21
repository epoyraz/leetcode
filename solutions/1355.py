class Solution(object):
    def minDeletion(self, nums):
        n = len(nums)
        deletions = 0
        B_len = 0
        prev = None
        for x in nums:
            if B_len % 2 == 0:
                prev = x
                B_len += 1
            else:
                if x != prev:
                    prev = x
                    B_len += 1
                else:
                    deletions += 1
        if B_len % 2 == 1:
            deletions += 1
        return deletions
