class MyCalendarTwo(object):
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, startTime, endTime):
        for os, oe in self.overlaps:
            if startTime < oe and endTime > os:
                return False
        for bs, be in self.bookings:
            if startTime < be and endTime > bs:
                self.overlaps.append((max(startTime, bs), min(endTime, be)))
        self.bookings.append((startTime, endTime))
        return True