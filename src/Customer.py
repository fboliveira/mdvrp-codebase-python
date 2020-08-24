class Customer:

    _id = int()
    _pointx = float()
    _pointy = float()
    _serviceDuration = float()
    _demand = int()

    def __init__(self, id, x, y, duration, demand):
        self._id = id
        self._pointx = x
        self._pointy = y
        self._serviceDuration = duration
        self._demand = demand

    def id(self):
        return self._id

    def x(self):
        return self._pointx

    def y(self):
        return self._pointy

    def serviceDuration(self):
        return self._serviceDuration

    def demand(self):
        return self._demand

    def doPrint(self):
        print(
            "Customer: ", self.id(), " - (", self.x(), ", ", self.y(),
            ") - Service duration: ", self.serviceDuration(),
            " - Demand: ", self.demand())
