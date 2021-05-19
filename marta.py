from DSVccm4 import DSVccm4
import numpy as np
import math
import csv
arrGeneticAlgorithmCCM4 = []
arrGeneticAlgorithmCCTimeM4 = []


with open('GACCm4cost71.csv', 'w') as f1, open('GACCm4time71.csv', 'w') as f2 :
    # create the csv writer
    writer1 = csv.writer(f1)
    writer2 = csv.writer(f2)
    for i in range(71, 100):
        print(i)
        j = math.ceil(i * 1.3)
        tC = math.floor(i * 0.15)
        cC = math.floor(j * 0.15)

        DSVccmFour = DSVccm4(i, j, tC, cC)
        gaCCM41, gaCCM42 = DSVccmFour.run(1, False)
        arrGeneticAlgorithmCCM4.append(gaCCM41)
        arrGeneticAlgorithmCCTimeM4.append(gaCCM42)
        # write a row to the csv file
        writer1.writerow(gaCCM41)
        writer2.writerow(gaCCM42)

#np.savetxt('GeneticAlgorithmCCM4.csv', np.array(arrGeneticAlgorithmCCM4), fmt="%s", delimiter=',')
#np.savetxt('GeneticAlgorithmCCTimeM4.csv', np.array(arrGeneticAlgorithmCCTimeM4), fmt="%s", delimiter=',')
