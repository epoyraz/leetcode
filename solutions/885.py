import bisect

class ExamRoom(object):
    def __init__(self, n):
        self.n = n
        self.seats = []

    def seat(self):
        if not self.seats:
            self.seats.append(0)
            return 0
        
        max_dist = self.seats[0]
        seat = 0

        for i in range(len(self.seats) - 1):
            dist = (self.seats[i+1] - self.seats[i]) // 2
            if dist > max_dist:
                max_dist = dist
                seat = self.seats[i] + dist

        if self.n - 1 - self.seats[-1] > max_dist:
            seat = self.n - 1

        bisect.insort(self.seats, seat)
        return seat

    def leave(self, p):
        self.seats.remove(p)
