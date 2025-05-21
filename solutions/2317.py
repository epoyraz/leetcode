class Solution(object):
    def countCollisions(self, directions):
        # Remove leading L and trailing R as they won't cause any collisions
        directions = directions.lstrip('L').rstrip('R')
        return sum(1 for c in directions if c != 'S')
