import random
from time import time
import numpy as np
from generator import Generator
import math
import matplotlib.pyplot as plt
class Utils:
    @staticmethod
    def swap_with_random(chromosome, cities, cc, idx1):

        new_list = [el for el in cities if el not in cc and el not in chromosome]
        random.shuffle(new_list)
        chromosome[idx1] = new_list[0]
        return chromosome

    @staticmethod
    def run(trucks,cities,tclist, cclist):

        tc = tclist
        cc= cclist
        rows = trucks


        chromosome = random.choices(cities, k=len(trucks))

        # here apply constraints
        count = 0
        for column in chromosome:
            if tc[count] ==1:
                if column in cc:
                    chromosome = Utils.swap_with_random(chromosome, cities, cc, count)
            count+=1

        zipped = zip(rows, chromosome)
        zipped = list(zipped)
        total = 0
        solution = []
        for (row, column) in zipped:
            solution.append(column)

        return solution


