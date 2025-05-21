class UndergroundSystem(object):

    def __init__(self):
        self.check_in_data = {}  # id -> (stationName, time)
        self.trip_data = {}      # (startStation, endStation) -> [total_time, trip_count]

    def checkIn(self, id, stationName, t):
        self.check_in_data[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start_station, start_time = self.check_in_data.pop(id)
        trip = (start_station, stationName)
        duration = t - start_time
        if trip not in self.trip_data:
            self.trip_data[trip] = [0, 0]
        self.trip_data[trip][0] += duration
        self.trip_data[trip][1] += 1

    def getAverageTime(self, startStation, endStation):
        total_time, trip_count = self.trip_data[(startStation, endStation)]
        return float(total_time) / trip_count
