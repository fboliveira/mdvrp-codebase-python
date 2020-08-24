# from Problem import Problem
class Route:

    _depot = int()
    _tour = None
    _cost = float()
    _penaltyDuration = float()
    _penaltyDemand = float()
    _totalDemand = int()
    _totalServiceTime = int()
    _problem = None

    def __init__(self, problem, depot):
        self._problem = problem
        self._depot = depot
        self._tour = []

    def startValues(self):
        self._cost = 0.0
        self._penaltyDuration = 0.0
        self._penaltyDemand = 0.0
        self._totalDemand = 0
        self._totalServiceTime = 0

    def append(self, customer):
        self._tour.append(customer)

    def calculateCost(self):
        demand = 0
        cost = 0.0
        service = 0

        if len(self._tour) > 0:

            # D -> C1
            customer = self._tour[0] - 1
            cost = cost + self._problem.depotDistance(self._depot, customer)

            # Cn -> D
            customer = self._tour[-1] - 1
            cost = cost + self._problem.depotDistance(self._depot, customer)

            for i in range(len(self._tour)):
                customer = self._tour[i] - 1
                if i + 1 < len(self._tour):
                    nextCustomer = self._tour[i + 1] - 1
                    cost = cost + \
                        self._problem.customerDistance(customer, nextCustomer)

                demand = demand + self._problem.customerDemand(customer)
                service = service + self._problem.customerService(customer)

        self._totalDemand = demand
        self._totalServiceTime = service
        self.updateCost(cost)

    def updateCost(self, cost):
        self._cost = cost
        self.updatePenalty()

    def updatePenalty(self):
        if self._totalDemand > self._problem.capacity():
            self._penaltyDemand = 1000.0 * \
                (self._totalDemand - self._problem.capacity())
        else:
            self._penaltyDemand = 0.0

        cost = self._cost + self._totalServiceTime

        if self._problem.duration() > 0 and cost > self._problem.duration():
            self._penaltyDuration = 1000.0 * \
                (self._totalServiceTime - self._problem.duration())
        else:
            self._penaltyDuration = 0.0

    def totalCost(self):
        return self._cost + self._penaltyDemand + self._penaltyDuration

    def doPrint(self):
        print(
            self._depot, "\t", "{:10.4f}".format(self.totalCost()), "\t", self._totalServiceTime,
            "\t(", "{:10.4f}".format(self.totalCost() + self._totalServiceTime), ")\t",
            self._totalDemand, "\t", end="")
        print(self._tour)
