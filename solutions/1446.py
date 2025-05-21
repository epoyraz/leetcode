class Solution:
    def angleClock(self, hour, minutes):
        # Calculate the angles of the hour and minute hands
        minute_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes
        
        # Compute the absolute difference
        diff = abs(hour_angle - minute_angle)
        # Return the smaller of diff and 360 - diff
        return min(diff, 360 - diff)
