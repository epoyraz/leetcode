class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        d = max(dx, dy)
        if t < d:
            return False
        # If start == finish, you need at least 2 moves to return after moving
        if d == 0 and t == 1:
            return False
        return True
