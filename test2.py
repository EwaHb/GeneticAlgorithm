from DSVccm4 import DSVccm4
import numpy as np
import math

arrGeneticAlgorithmCCM4 = []
arrGeneticAlgorithmCCTimeM4 = []

for i in range(5, 15):
    print(i)
    j = math.ceil(i * 1.3)
    tC = math.floor(i * 0.15)
    cC = math.floor(j * 0.15)

    DSVccmFour = DSVccm4(i, j, tC, cC)
    gaCCM41, gaCCM42 = DSVccmFour.run(1, False)
    arrGeneticAlgorithmCCM4.append(gaCCM41)
    arrGeneticAlgorithmCCTimeM4.append(gaCCM42)


np.savetxt('GeneticAlgorithmCCM4.csv', np.array(arrGeneticAlgorithmCCM4), fmt="%s", delimiter=',')
np.savetxt('GeneticAlgorithmCCTimeM4.csv', np.array(arrGeneticAlgorithmCCTimeM4), fmt="%s", delimiter=',')
