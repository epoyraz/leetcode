class Solution(object):
    def fallingSquares(self, positions):
        ans = []
        intervals = []
        max_height = 0
        
        for left, size in positions:
            right = left + size
            height = size
            for l, r, h in intervals:
                if not (right <= l or left >= r):
                    height = max(height, h + size)
            intervals.append((left, right, height))
            max_height = max(max_height, height)
            ans.append(max_height)
        
        return ans
