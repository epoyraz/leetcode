class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / float(s) for p, s in cars]

        fleets = 0
        curr_time = 0
        for time in times:
            if time > curr_time:
                fleets += 1
                curr_time = time
        return fleets
