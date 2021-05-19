import random
from time import time
import numpy as np
from generator import Generator
import math

class RandomSolutionCC:
    @staticmethod
    def swap_with_random(chromosome, cities, cc, idx1):

        new_list = [el for el in list(range(cities)) if el not in cc and el not in chromosome]
        #random.shuffle(new_list)
        #print(new_list)
        chromosome[idx1] = new_list[0]
        '''
        if len(new_list) <= 1:
            # what if this random is already in the list, needs to be fixed
            new_list = [el for el in list(range(len(cities))) if el not in cc]
            i2 = random.choice(new_list)
            idx = range(len(chromosome))
            idx2 = random.choice(idx)
            chromosome[idx1] = i1
            chromosome[idx2] = i2
        else:
            i1, i2 = random.sample(new_list, 2)
            i1 = chromosome.index(i1)
            i2 = chromosome.index(i2)
            chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]
        '''
        return chromosome

    @staticmethod
    #def run(trucks, cities):
    def run(trucks,cities,tcNb, ccNb):
        tiempo_inicial_t2 = time()
        print(
            "--------------------------------------------------------- Random Solution with a Country Constraint--------------------------------------------------------- \n")
        globTotal = math.inf
        globSolution= math.inf
        #matrix = Generator.generateHA(trucks, cities)
        matrix, cc, tc = Generator.generateSRSCC(trucks, cities, tcNb, ccNb)
        rows = list(range(0, trucks))
        for i in range(40000):
            clients = list(range(0, cities-1))
            columns = random.choices(clients, k=trucks)

            # here apply constraints
            count = 0
            for column in columns:
                if tc[count] ==1:
                    if column in cc:
                        columns = RandomSolutionCC.swap_with_random(columns, cities, cc, count)
                count+=1

            zipped = zip(rows, columns)
            zipped = list(zipped)
            total = 0
            solution = []
            for (row, column) in zipped:
                value = matrix[row][column]
                if tc[row] == 1:
                    if column in cc:
                        value+=math.inf
                total += value
                solution.append(str('truck '+ str(row) +'---> customer ' + str(column)))
            if total < globTotal:
                globTotal = total
                globSolution = solution
        print('tc')
        print(tc)
        print('cc')
        print(cc)
        print("Solution:", globSolution)
        print("Total allocation cost:",globTotal)
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        print("Total time: ", total_time, " secs.\n")
        return globTotal, total_time


RandomSolutionCC.run(30,40,3,5)

'''
        def random_replace_mutation_two(chromosome_aux):
            chromosome = chromosome_aux
            idx = range(len(chromosome))
            i1, i2 = random.sample(idx, 2)
            repl = [chromosome[i1],chromosome[i2]] + cc
            temp = Diff(self.genes,repl)
            chromosome[i1], chromosome[i2] = random.sample(temp, 2)
            return chromosome
'''