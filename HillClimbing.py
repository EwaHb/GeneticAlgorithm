import random
from random import randrange
from time import time
import numpy as np
import math

from generator import Generator


class HillClimbing:
    def __init__(self, trucks, cities):
        self.trucksM, self.trucks, self.cities = Generator.generateGA(trucks,cities)
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
            routeLength += self.distanceTrip(i, solution[i])
        return routeLength

    def distanceTrip(self, index, city):
        w = self.trucksM[index]
        return w[city]

    def getNeighbours(self, solution):
        neighbours = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution.copy()
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
        print(currentSolution)
        return currentSolution, currentRouteLength

    def printhc(self, currentSolution, currentRouteLength):
        solution = []
        for i in range(len(currentSolution)):
            solution.append(str('truck ' + str(i) + '---> customer ' + str(currentSolution[i])))
        print("Solution:", solution)
        print("Total allocation cost:", currentRouteLength)


class HillClimbingrun:
    def __init__(self, trucks, cities):
        self.trucks = trucks
        self.cities = cities

    def runHillClimbing(self, param):
        tiempo_inicial_t2 = time()
        bestCost = math.inf
        print(
            "--------------------------------------------------------- Hill Climbing --------------------------------------------------------- \n")
        for i in range(param):
            localHillClimbing = HillClimbing(self.trucks, self.cities)
            localHillClimbing.run()
            if localHillClimbing.currentRouteLength < bestCost:
                bestCost = localHillClimbing.currentRouteLength
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        #print("Mean cost for ", param, "episodes: ", totalCost / param)
        print("Total cost ", bestCost)
        print("Total time: ", total_time, " secs.\n")
        # return solution
        return bestCost, total_time

obj = HillClimbingrun(10,13)
obj.runHillClimbing(1)


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