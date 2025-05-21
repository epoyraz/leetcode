class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stops = [0] * 1001  # Since max location is 1000

        for num_passengers, start, end in trips:
            stops[start] += num_passengers
            stops[end] -= num_passengers

        current_passengers = 0
        for p in stops:
            current_passengers += p
            if current_passengers > capacity:
                return False

        return True
