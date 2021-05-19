from munkres import Munkres, print_matrix
from time import time
import numpy as np
from generator import Generator


class Hungarian:
    @staticmethod
    def hungarian(trucks, cities):
        print(
            "--------------------------------------------------------- Hungarian Algorithm --------------------------------------------------------- \n")
        m = Munkres()
        matrix = Generator.generateHA(trucks,cities)
        tiempo_inicial_t2 = time()
        indexes = m.compute(matrix)
        solution = []
        total = 0
        for row, column in indexes:
            value = matrix[row][column]
            total += value
            solution.append(str('truck '+ str(row) +'---> customer ' + str(column)))
        print("Solution:", solution)
        print("Total allocation cost:",total)
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        print("Total time: ", total_time , " secs.\n")
        return total, total_time
#Hungarian.hungarian(5,5)
