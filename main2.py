from HillClimbingCC import HillClimbingCCrun
from HillClimbing import HillClimbingrun
from hungarian import Hungarian
from DSV import DSVsimple

from DSVm4 import DSVm4

from DSVccm4 import DSVccm4
from DSVm1 import DSVm1
from DSVm2 import DSVm2
from DSVm3 import DSVm3
from DSVcc import DSVcc
from DSVccm1 import DSVccm1
from DSVccm2 import DSVccm2
from DSVccm3 import DSVccm3
from simpleRandomSolution import RandomSolution
from SimpleRandomSolutionCC import RandomSolutionCC
import matplotlib.pyplot as plt
import numpy as np
import math

arrGeneticAlgorithmM1 = []

for i in range(5, 7):
    customers = [math.ceil(i * 1.1), math.ceil(i * 1.3), math.ceil(i * 1.5)]
    j = math.ceil(i*1.3)
    print(i)
    print(j)

    DSVmOne = DSVm1(i, j)
    gaM11, gaM12 = DSVmOne.run(1, False)
    arrGeneticAlgorithmM1.append(gaM11)


np.savetxt('files/GeneticAlgorithmM1.csv', np.array(arrGeneticAlgorithmM1), fmt="%s", delimiter=',')

