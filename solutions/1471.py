class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        # Precompute valid seat bitmasks for each row
        valid_row_masks = []
        for i in range(m):
            good = 0
            for j in range(n):
                if seats[i][j] == '.':
                    good |= (1 << j)
            row_masks = []
            # Enumerate all subsets of good seats
            mask = good
            sub = mask
            while True:
                # Check no two adjacent students in the same row
                if (sub & (sub << 1)) == 0:
                    row_masks.append(sub)
                if sub == 0:
                    break
                sub = (sub - 1) & good
            valid_row_masks.append(row_masks)
        
        # DP: dp_prev[mask] = max students up to previous row ending with mask
        dp_prev = {mask: bin(mask).count('1') for mask in valid_row_masks[0]}
        
        for i in range(1, m):
            dp_curr = {}
            for mask in valid_row_masks[i]:
                cnt = bin(mask).count('1')
                best = 0
                for pmask, val in dp_prev.items():
                    # No cheating diagonally with previous row
                    if (mask & (pmask << 1)) == 0 and (mask & (pmask >> 1)) == 0:
                        best = max(best, val)
                dp_curr[mask] = best + cnt
            dp_prev = dp_curr
        
        # Result is the maximum over the last row's masks
        return max(dp_prev.values() or [0])
