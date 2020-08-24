''' 

A solution selected here for representating this problem is a simple collection (list) of routes. Each routes has a list of clients (tour) and the associated depot. As the problem is homogeneous, a representation for vehicles is not necessary. For future implementations of , this must be considered.

'''

import math
from Route import Route

class Solution:

    _routes = []
    _problem = None
    _cost = math.inf

    def __init__(self, problem):
        self._problem = problem

    def addRoute(self, route):
        self._routes.append(route)

    def calculateCost(self):
        self._cost = 0.0
        for route in range(len(self._routes)):
            route.calculateCost()
            self._cost += route.totalCost()

    def totalCost(self):
        self.calculateCost()
        return self._cost