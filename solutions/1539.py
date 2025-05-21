from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums):
        diagonals = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
        
        result = []
        for k in sorted(diagonals):
            result.extend(reversed(diagonals[k]))
        
        return result
