'''

import matplotlib.pyplot as plt

import numpy as np
from DSVm3 import DSVm3
from DSVm1 import DSVm1
from DSVm2 import DSVm2
from DSVm4 import DSVm4
import math
from simpleRandomSolution import RandomSolution

DSVm1 = DSVm1(7, 13)
DSVm1.run(10,False)

DSVm2 = DSVm2(7, 13)
DSVm2.run(10,False)

DSVm3 = DSVm3(7, 13)
DSVm3.run(10,False)

RandomSolution.run(7, 13)

DSVm4 = DSVm4(7, 13)
DSVm4.run(1,True)

[2452, 2452, 2452, 2452, 2182, 1543, 2254, 2152, 1543, 1543, 1543, 1543, 1543, 1543, 1543, 1543, 1543, 1509, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422, 1422]


'''

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import csv
import torch
import numpy as np
from DSVm4 import DSVm4
import math


arrGeneticAlgorithmM1 = []

two_dim_arr = []  # each line of the file is an array element
with open('GeneticAlgorithmM1.csv', 'r') as record_read:
    reader = csv.reader(record_read)
    for i, each_arr in enumerate(reader):
        vari = [eval(each) for each in each_arr]
        two_dim_arr.append(vari)

print('len two_dim_arr')
print(len(two_dim_arr))
