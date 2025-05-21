import math

class Solution:
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        px, py = location
        same_spot = 0
        angles = []

        # 1) Separate points at the observer location
        for x, y in points:
            dx, dy = x - px, y - py
            if dx == 0 and dy == 0:
                same_spot += 1
            else:
                # compute angle in degrees from east
                theta = math.degrees(math.atan2(dy, dx))
                if theta < 0:
                    theta += 360
                angles.append(theta)

        # 2) Sort the angles and duplicate with +360 for wraparound
        angles.sort()
        m = len(angles)
        angles += [a + 360 for a in angles]

        # 3) Two-pointer sweep to find max points in any angle-window
        best = 0
        left = 0
        for right in range(len(angles)):
            # shrink window from left if it exceeds the allowed angle
            while angles[right] - angles[left] > angle:
                left += 1
            # window [left..right] is within 'angle'
            best = max(best, right - left + 1)

        # 4) include points at the same spot (always visible)
        return best + same_spot
