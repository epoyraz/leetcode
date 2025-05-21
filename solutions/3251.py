class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = -1
        max_area = 0
        for l, w in dimensions:
            diag_sq = l * l + w * w
            area = l * w
            if diag_sq > max_diag:
                max_diag = diag_sq
                max_area = area
            elif diag_sq == max_diag:
                max_area = max(max_area, area)
        return max_area
