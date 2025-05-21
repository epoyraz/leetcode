class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]  # [rowIndex, maxOnesCount]
        """
        max_count = -1
        best_row = 0
        
        for i, row in enumerate(mat):
            cnt = sum(row)  # since row entries are 0 or 1
            if cnt > max_count:
                max_count = cnt
                best_row = i
        
        return [best_row, max_count]
