# Depots


class Depot:

    _id = int()
    _pointx = float()
    _pointy = float()
    _duration = float()
    _capacity = int()

    def __init__(self, id, x, y, duration, capacity):
        self._id = id
        self._pointx = x
        self._pointy = y
        self._duration = duration
        self._capacity = capacity

    def id(self):
        return self._id

    def x(self):
        return self._pointx

    def y(self):
        return self._pointy

    def duration(self):
        return self._duration

    def capacity(self):
        return self._capacity

    def doPrint(self):
        print(
            "Depot: ", self.id(), " - (", self.x(), ", ", self.y(),
            ") - Duration: ", self.duration(),
            " - Capacity: ", self.capacity())
