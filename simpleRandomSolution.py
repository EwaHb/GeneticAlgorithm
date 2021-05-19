import random
from time import time
import numpy as np
from generator import Generator
import math

class RandomSolution:

    @staticmethod
    def run(trucks,cities):
        tiempo_inicial_t2 = time()
        print(
            "--------------------------------------------------------- Random Solution --------------------------------------------------------- \n")
        def zerolistmaker(n):
            listofzeros = [0] * n
            return listofzeros
        globTotal = math.inf
        globSolution= math.inf
        matrix = Generator.generateHA(trucks, cities)
        rows = list(range(0, trucks))
        for i in range(40000):
            clients = list(range(0, cities-1))
            columns = random.choices(clients, k=trucks)
            zipped = zip(rows, columns)
            zipped = list(zipped)
            total = 0
            solution = []
            for (row, column) in zipped:
                value = matrix[row][column]
                total += value
                solution.append(str('truck '+ str(row) +'---> customer ' + str(column)))
            if total < globTotal:
                globTotal = total
                globSolution = solution
        print("Solution:", globSolution)
        print("Total allocation cost:",globTotal)
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        print("Total time: ", total_time, " secs.\n")
        return globTotal, total_time



