import random
from random import randrange
from time import time
import numpy as np
import math

from generator import Generator


class HillClimbingCC:
    def __init__(self, trucks, cities, cc, tc):
        self.trucksM, self.trucks, self.cities, self.cclist, self.tclist = Generator.generateGAcc(trucks, cities, cc,
                                                                                                  tc)
        self.currentRouteLength = None
        '''
        print(self.tclist)
        print(self.cclist)
        '''

    def randomSolution(self):
        citiesInn = self.cities
        solution = []
        for i in range(len(self.trucks)):
            randomCity = citiesInn[random.randint(0, len(citiesInn) - 1)]
            solution.append(randomCity)
            citiesInn.remove(randomCity)
        return solution

    def routeLength(self, solution):
        routeLength = 0
        for i in range(len(solution)):
            if self.tclist[i] == 1:
                if solution[i] in self.cclist:
                    routeLength += 1000
            routeLength += self.distanceTrip(i, solution[i])
        return routeLength

    def distanceTrip(self, index, city):
        w = self.trucksM[index]
        return w[city]

    def find_nearest_i(self, i):
        while self.tclist[i] == 1:
            if i == len(self.tclist) - 1:
                i = 0
            else:
                i += 1
        return i

    def find_nearest_j(self, solution, i, j):
        while self.tclist[j] == 1:
            if solution[i] in self.cclist:
                if j == len(solution) - 1:
                    j = self.find_nearest_i(0)
                else:
                    j += 1
            else:
                return j
        return j

    def getNeighbours(self, solution):
        neighbours = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution.copy()
                i = self.find_nearest_i(i)
                j = self.find_nearest_j(solution, i, j)
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                neighbours.append(neighbour)
        return neighbours

    def getBestNeighbour(self, neighbours):
        bestRouteLength = self.routeLength(neighbours[0])
        bestNeighbour = neighbours[0]
        for neighbour in neighbours:
            currentRouteLength = self.routeLength(neighbour)
            if currentRouteLength < bestRouteLength:
                bestRouteLength = currentRouteLength
                bestNeighbour = neighbour
        return bestNeighbour, bestRouteLength

    def run(self):

        currentSolution = self.randomSolution()
        currentRouteLength = self.routeLength(currentSolution)
        neighbours = self.getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = self.getBestNeighbour(neighbours)

        while bestNeighbourRouteLength < currentRouteLength:
            currentSolution = bestNeighbour
            currentRouteLength = bestNeighbourRouteLength
            neighbours = self.getNeighbours(currentSolution)
            bestNeighbour, bestNeighbourRouteLength = self.getBestNeighbour(neighbours)

        # self.printhc(currentSolution, currentRouteLength)
        self.currentRouteLength = currentRouteLength
        return currentSolution, currentRouteLength

    def printhc(self, currentSolution, currentRouteLength):
        solution = []
        for i in range(len(currentSolution)):
            solution.append(str('truck ' + str(i) + '---> customer ' + str(currentSolution[i])))
        print("Solution:", solution)
        print("Total allocation cost:", currentRouteLength)


class HillClimbingCCrun:
    def __init__(self, trucks, cities, cc, tc):
        self.trucks = trucks
        self.cities = cities
        self.cc = cc
        self.tc = tc

    def runHillClimbingcc(self, param):
        tiempo_inicial_t2 = time()
        bestCost = math.inf
        print(
            "--------------------------------------------------------- Hill Climbing with a Country Constraint --------------------------------------------------------- \n")
        for i in range(param):
            SimpleHillClimbing = HillClimbingCC(self.trucks, self.cities, self.cc, self.tc)
            SimpleHillClimbing.run()
            if SimpleHillClimbing.currentRouteLength < bestCost:
                bestCost = SimpleHillClimbing.currentRouteLength
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        #print("Mean cost for ", param, "episodes: ", totalCost / param)
        print("Total cost ", bestCost)
        print("Total time: ", total_time, " secs.\n")
        return bestCost, total_time


# obj = SimpleHillClimbing(10,20,5,6)
# obj.hillClimbing()


'''
def find_nearest_i(solution, i):
    while tclist[i] ==1:


        print('infinite loop 1')
        if solution[j] in cclist:
            print('infinite loop 2')
            i+=1
        else:
            return i

    return i
'''