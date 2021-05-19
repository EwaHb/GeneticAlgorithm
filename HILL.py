import random
from random import randrange
from time import time
import numpy as np

from generator import Generator

'''
class Hill:
       def __init__(self, trucks, cities):
        self.trucksM, self.trucks, self.cities = Generator.generateGA(trucks,cities)
'''
trucksM, trucks, cities = Generator.generateGA(10, 20)
print(trucksM, trucks, cities)
trucklen = len(trucks)


# citieslen = len(cities)

def randomSolution(trucks, cities):
    # cities = list(range(len(trucksM)))
    # cities = list(range(cities))
    solution = []

    for i in range(trucklen):
        citieslen = len(cities)
        print('citieslen')
        print(citieslen)
        print('i')
        print(i)
        print('cities')
        print(cities)
        randomCity = cities[random.randint(0, citieslen - 1)]
        print('randomCity')
        print(randomCity)
        solution.append(randomCity)
        cities.remove(randomCity)
    print(solution)
    return solution


def routeLength(trucksM, solution):
    routeLength = 0
    for i in range(len(solution)):
        # routeLength += tsp[solution[i - 1]][solution[i]]
        routeLength += distanceTrip(i, solution[i])
        print('routeLength')
        print(routeLength)
    return routeLength


# distanceTrip(i, chromosome[i])

def distanceTrip(index, city):
    print('distanceTriindex')
    print(index)
    print('distanceTripCity')
    print(city)
    w = trucksM[index]
    print('w[city]')
    print(w[city])
    return w[city]


def getNeighbours(solution):
    neighbours = []
    solutionlen = len(solution)
    pos = solution[random.randint(0, solutionlen - 1)]
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            print(neighbour)
            print('neighbour')
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(trucksM, neighbours):
    bestRouteLength = routeLength(trucksM, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(trucksM, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    print('bestNeightbour')
    print(bestNeighbour)
    return bestNeighbour, bestRouteLength


# solution  = randomSolution(trucks,cities)
# routeLength(trucksM, solution)
# neighbours = getNeighbours(solution)
# getBestNeighbour(trucksM, neighbours)

def hillClimbing(trucksM):
    currentSolution = randomSolution(trucksM, cities)
    currentRouteLength = routeLength(trucksM, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(trucksM, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(trucksM, neighbours)

    print('currentSolution, currentRouteLength')
    print(currentSolution, currentRouteLength)
    return currentSolution, currentRouteLength


hillClimbing(trucksM)
