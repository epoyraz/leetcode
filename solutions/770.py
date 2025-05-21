class Solution(object):
    def minSwapsCouples(self, row):
        n = len(row) // 2
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        
        for i in range(0, len(row), 2):
            first = row[i]
            partner = first ^ 1  # partner is first ^ 1 (0->1, 1->0, 2->3, 3->2, etc.)
            if row[i+1] != partner:
                swaps += 1
                partner_idx = pos[partner]
                
                # swap row[i+1] with row[partner_idx]
                row[i+1], row[partner_idx] = row[partner_idx], row[i+1]
                
                # update positions
                pos[row[partner_idx]] = partner_idx
                pos[row[i+1]] = i+1
        
        return swaps
