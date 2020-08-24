import numpy as np
import numpy.matlib
import math
import os.path

from Customer import Customer
from Depot import Depot
from Config import Config

class Problem:

    TYPE = "MDVRP"

    _instance = None
    _bestKnownSolution = float()
    _vehicles = int()
    _customers = int()
    _depots = int()

    # Homogeneous fleet
    _duration = float()
    _capacity = int()

    _customersList = []
    _depotsList = []

    _customerDistances = None
    _depotDistances = None

    def __init__(self, instance):
        self._instance = instance
        self._customersList = []
        self._depotsList = []        

    @property
    def instance(self):
        return self._instance

    @property
    def capacity(self):
        return self._capacity

    @property
    def duration(self):
        return self._duration

    @property
    def customers(self):
        return self._customers

    @property
    def customer(self, id):
        return self._customersList[id]

    @property
    def depots(self):
        return self._depots

    @property
    def vehicles(self):
        return self._vehicles

    @property
    def depotDistance(self, depot, customer):
        return self._depotDistances[depot, customer]

    @property
    def customerDistance(self, ci, cj):
        return self._customerDistances[ci, cj]

    @property
    def customerDemand(self, customer):
        return self._customersList[customer].demand()

    @property
    def customerService(self, customer):
        return self._customersList[customer].serviceDuration()

    @property
    def bks(self):
        return self._bestKnownSolution

    # The instances and their descriptions may be found in: https://github.com/fboliveira/MDVRP-Instances
    def processInstanceFiles(self):
        instanceFile = Config.instance().datPath + '/' + self.instance
        solutionFile = Config.instance().solPath + '/' + self.instance + ".res"

        dataInstance = open(instanceFile)
        dataSolution = open(solutionFile)

        # Best known solution - literature
        self._bestKnownSolution = float(dataSolution.readline())
        dataSolution.close()

        for i, line in enumerate(dataInstance):
            ln = line.split()

            if i == 0:
                # Problem informations
                self._vehicles = int(ln[1])
                self._customers = int(ln[2])
                self._depots = int(ln[3])
            elif i == 1:
                # Capacity and duration - homogeneous problems
                self._duration = float(ln[0])
                self._capacity = int(ln[1])
            elif i > self._depots:
                # After capacity and duration lines
                # Id, X, Y, service duration, demand
                id = int(ln[0])
                x = float(ln[1])
                y = float(ln[2])

                if id <= self._customers:
                    # Customers
                    duration = int(ln[3])
                    demand = int(ln[4])
                    c = Customer(id, x, y, duration, demand)
                    self._customersList.append(c)
                else:
                    # Depots
                    id = id - self._customers
                    d = Depot(id, x, y, self._duration, self._capacity)
                    self._depotsList.append(d)

        dataInstance.close()
        self.calculateDistances()

    def calculateEuc2D(self, x1, y1, x2, y2):
        xd = x1 - x2
        yd = y1 - y2

        xd = xd ** 2
        yd = yd ** 2

        return math.sqrt(xd + yd)

    def calculateDistances(self):
        self._customerDistances = \
            numpy.matlib.zeros((self._customers, self._customers))
        self._depotDistances = numpy.matlib.zeros(
            (self._depots, self._customers))

        # Customers X customers
        for ci in self._customersList:
            for cj in self._customersList:

                if ci.id() != cj.id():
                    dist = self.calculateEuc2D(ci.x(), ci.y(), cj.x(), cj.y())
                else:
                    dist = math.inf

                self._customerDistances[ci.id() - 1, cj.id() - 1] = dist

        # Depots X customers
        for d in self._depotsList:
            for c in self._customersList:
                dist = self.calculateEuc2D(d.x(), d.y(), c.x(), c.y())
                self._depotDistances[d.id() - 1, c.id() - 1] = dist

    def pLine(self):
        print('-' * 50)

    def print(self):
        self.pLine()
        print("Instance = ", self._instance)
        print("Best known solution = ", self._bestKnownSolution)
        print("Depots = ", self._depots)
        print("Vehicle = ", self._vehicles)
        print("Customers = ", self._customers)
        self.pLine()

        for d in self._depotsList:
            d.doPrint()

        for c in self._customersList:
            c.doPrint()

        self.pLine()
        print("Distances - DEPOTS x CUSTOMERS")
        print(self._depotDistances)
        self.pLine()
        print("Distances - CUSTOMERS x CUSTOMERS")
        print(self._customerDistances)
        self.pLine()
