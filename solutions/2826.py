class Solution:
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        # map each row-mask (0â¦2^nâ1) to one example index
        mask_to_idx = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, bit in enumerate(row):
                mask |= (bit << j)
            # only keep the first index we see for each mask
            if mask not in mask_to_idx:
                mask_to_idx[mask] = i

        # 1) Any all-zero row is a valid subset of size 1
        if 0 in mask_to_idx:
            return [mask_to_idx[0]]

        # 2) Otherwise look for any two rows whose masks don't overlap
        masks = list(mask_to_idx)
        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                if (masks[i] & masks[j]) == 0:
                    idx1 = mask_to_idx[masks[i]]
                    idx2 = mask_to_idx[masks[j]]
                    return sorted([idx1, idx2])

        # 3) No valid subset
        return []
