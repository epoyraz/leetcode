class ParkingSystem:
    def __init__(self, big, medium, small):
        # capacities for each car type
        self.cap = [0, big, medium, small]
        # current parked counts
        self.count = [0, 0, 0, 0]

    def addCar(self, carType):
        if self.count[carType] < self.cap[carType]:
            self.count[carType] += 1
            return True
        return False
