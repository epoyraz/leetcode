class Solution:
    def canChange(self, start, target):
        # collect non-blank pieces and their positions
        s_pos, t_pos = [], []
        for i, c in enumerate(start):
            if c != '_':
                s_pos.append((c, i))
        for i, c in enumerate(target):
            if c != '_':
                t_pos.append((c, i))
        
        # must have the same sequence of pieces
        if len(s_pos) != len(t_pos):
            return False
        
        # check each piece's movement feasibility
        for (c1, i1), (c2, i2) in zip(s_pos, t_pos):
            if c1 != c2:
                return False
            # 'L' can only move left: start index >= target index
            if c1 == 'L' and i1 < i2:
                return False
            # 'R' can only move right: start index <= target index
            if c1 == 'R' and i1 > i2:
                return False
        
        return True
