import itertools

class Solution:
    def maximumRows(self, matrix, numSelect):
        m = len(matrix)
        n = len(matrix[0])
        # Precompute a bitmask for each row where bits set correspond to 1s
        row_masks = []
        for row in matrix:
            mask = 0
            for j, val in enumerate(row):
                if val:
                    mask |= 1 << j
            row_masks.append(mask)
        
        max_covered = 0
        # Iterate over all combinations of numSelect columns
        for cols in itertools.combinations(range(n), numSelect):
            # Build a mask with those columns selected
            sel_mask = 0
            for j in cols:
                sel_mask |= 1 << j
            
            # Count how many rows are fully covered by sel_mask
            covered = 0
            for rm in row_masks:
                # A row is covered if all 1-bits in rm are within sel_mask
                if rm & ~sel_mask == 0:
                    covered += 1
            
            if covered > max_covered:
                max_covered = covered
        
        return max_covered
