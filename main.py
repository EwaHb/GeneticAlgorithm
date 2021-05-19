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

arr = []
arrHungarian = []
arrHungarianTime = []
arrRandomSolution = []
arrRandomSolutionTime = []
arrRandomSolutionCC = []
arrRandomSolutionCCTime = []
arrHillClimbing = []
arrHillClimbingTime = []
arrHillClimbingCC = []
arrHillClimbingCCTime = []
arrGeneticAlgorithm = []
arrGeneticAlgorithmM1 = []
arrGeneticAlgorithmTimeM1 = []
arrGeneticAlgorithmM2 = []
arrGeneticAlgorithmTimeM2 = []
arrGeneticAlgorithmM3 = []
arrGeneticAlgorithmTimeM3 = []
arrGeneticAlgorithmTime = []
arrGeneticAlgorithmCC = []
arrGeneticAlgorithmTimeCC = []
arrGeneticAlgorithmCCM1 = []
arrGeneticAlgorithmTimeCCM1 = []
arrGeneticAlgorithmCCM2 = []
arrGeneticAlgorithmTimeCCM2 = []
arrGeneticAlgorithmCCM3 = []
arrGeneticAlgorithmTimeCCM3 = []
arrGeneticAlgorithmM4 = []
arrGeneticAlgorithmTimeM4 = []
arrGeneticAlgorithmCCM4 = []
arrGeneticAlgorithmCCTimeM4 = []



for i in range(5, 7):
    customers = [math.ceil(i * 1.1), math.ceil(i * 1.3), math.ceil(i * 1.5)]
    tC = math.ceil(i * 0.15)
    for j in customers:
        cC = math.ceil(j * 0.15)
        print(i)
        print(j)
        print(tC)
        print(cC)
        '''
        h1, h2 = Hungarian.hungarian(i, j)
        arrHungarian.append(h1)
        arrHungarianTime.append(h2)

        rs1, rs2 = RandomSolution.run(i, j)
        arrRandomSolution.append(rs1)
        arrRandomSolutionTime.append(rs2)

        HillClimbing = HillClimbingrun(i, j)
        hc1, hc2 = HillClimbing.runHillClimbing(1)
        arrHillClimbing.append(hc1)
        arrHillClimbingTime.append(hc2)

        HillClimbingCC = HillClimbingCCrun(i, j, tC, cC)
        hcCC1, hcCC2 = HillClimbingCC.runHillClimbingcc(1)
        arrHillClimbingCC.append(hcCC1)
        arrHillClimbingTime.append(hcCC2)

        '''

        DSVmOne = DSVm1(i, j)
        gaM11, gaM12 = DSVmOne.run(1, False)
        arrGeneticAlgorithmM1.append(gaM11)
        arrGeneticAlgorithmTime.append(gaM12)
        '''
        DSVmTwo = DSVm2(i, j)
        gaM21, gaM22 = DSVmTwo.run(1, False)
        arrGeneticAlgorithmM2.append(gaM21)
        arrGeneticAlgorithmTimeM2.append(gaM22)

        DSVmThree = DSVm3(i, j)
        gaM31, gaM32 = DSVmThree.run(1, False)
        arrGeneticAlgorithmM2.append(gaM31)
        arrGeneticAlgorithmTimeM2.append(gaM32)

        DSVproblemCCmOne = DSVccm1(i, j, tC, cC)
        gaCCm11, gaCCm12 = DSVproblemCCmOne.run(1, False)
        arrGeneticAlgorithmCCM1.append(gaCCm11)
        arrGeneticAlgorithmTimeCCM1.append(gaCCm12)

        DSVproblemCCmTwo = DSVccm2(i, j, tC, cC)
        gaCCm21, gaCCm22 = DSVproblemCCmTwo.run(1, False)
        arrGeneticAlgorithmCCM2.append(gaCCm21)
        arrGeneticAlgorithmTimeCCM2.append(gaCCm22)

        DSVproblemCCmThree = DSVccm3(i, j, tC, cC)
        gaCCm31, gaCCm32 = DSVproblemCCmThree.run(1, False)
        arrGeneticAlgorithmCCM3.append(gaCCm31)
        arrGeneticAlgorithmTimeCCM3.append(gaCCm32)

        DSVmFour = DSVm4(i, j)
        gaM41, gaM42 = DSVmFour.run(1, False)
        arrGeneticAlgorithmM4.append(gaM11)
        arrGeneticAlgorithmTimeM4.append(gaM12)

        DSVccmFour = DSVccm4(i, j,tC, cC)
        gaCCM41, gaCCM42 = DSVccmFour.run(1, False)
        arrGeneticAlgorithmCCM4.append(gaCCM41)
        arrGeneticAlgorithmCCTimeM4.append(gaCCM42)

        '''


np.savetxt('files/GeneticAlgorithmM1.csv', np.array(arrGeneticAlgorithmM1), fmt="%s", delimiter=',')

'''
np.savetxt('files/GeneticAlgorithmCCM1.csv', np.array(arrGeneticAlgorithmCCM1), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmCCTimeM1.csv', np.array(arrGeneticAlgorithmTimeCCM1), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmCCM2.csv', np.array(arrGeneticAlgorithmCCM2), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmCCTimeM2.csv', np.array(arrGeneticAlgorithmTimeCCM2), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmCCM3.csv', np.array(arrGeneticAlgorithmCCM3), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmCCTimeM3.csv', np.array(arrGeneticAlgorithmTimeCCM3), fmt="%s", delimiter=',')

np.savetxt('files/RandomSolution.csv', np.array(arrRandomSolution), fmt="%s", delimiter=',')
np.savetxt('files/RandomSolutionCC.csv', np.array(arrRandomSolutionCC), fmt="%s", delimiter=',')
np.savetxt('files/HillClimbing.csv', np.array(arrHillClimbing), fmt="%s", delimiter=',')
np.savetxt('files/HillClimbingCC.csv', np.array(arrHillClimbingCC), fmt="%s", delimiter=',')
np.savetxt('files/HungarianAlgorithm.csv', np.array(arrHungarian), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmTimeM1.csv', np.array(arrGeneticAlgorithmTimeM1), fmt="%s", delimiter=',')

np.savetxt('files/GeneticAlgorithmM2.csv', np.array(arrGeneticAlgorithmM2), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmTimeM2.csv', np.array(arrGeneticAlgorithmTimeM2), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmTimeM2.csv', np.array(arrGeneticAlgorithmTimeM2), fmt="%s", delimiter=',')
np.savetxt('files/GeneticAlgorithmTimeM3.csv', np.array(arrGeneticAlgorithmTimeM3), fmt="%s", delimiter=',')

np.savetxt('files/arrGeneticAlgorithmTimeM4.csv', np.array(arrGeneticAlgorithmTimeM4), fmt="%s", delimiter=',')
np.savetxt('files/arrGeneticAlgorithmM4.csv', np.array(arrGeneticAlgorithmM4), fmt="%s", delimiter=',')
np.savetxt('files/arrGeneticAlgorithmCCTimeM4.csv', np.array(arrGeneticAlgorithmCCTimeM4), fmt="%s", delimiter=',')
np.savetxt('files/arrGeneticAlgorithmCCM4.csv', np.array(arrGeneticAlgorithmCCM4), fmt="%s", delimiter=',')
'''
'''
rsCC1, rsCC2 = RandomSolutionCC.run(i, j, tC, cC)
arrRandomSolutionCC.append(rsCC1)
arrRandomSolutionCCTime.append(rsCC2)
'''