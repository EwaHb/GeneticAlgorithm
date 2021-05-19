import numpy as np
import random

#class generator():

'''
    def __init__(self, trucks, cities):
        self.trucks = trucks
        self.cities = cities
'''
class Generator:
        @staticmethod
        def generateGA(trucks, cities):
                np.random.seed(0)

                trucksM = np.random.randint(50,1500, size=(trucks, cities))
                trucks = list(range(trucks))
                cities = list(range(cities))
                return trucksM, trucks, cities

        @staticmethod
        def generateGAcc(trucks, cities,tcNb, ccNb):
                np.random.seed(0)
                def zerolistmaker(n):
                        listofzeros = [0] * n
                        return listofzeros

                def generateRandom(start,end):
                        ran = random.randint(start, end)
                        return ran


                trucksM = np.random.randint(50,1500, size=(trucks, cities))
                trucks = list(range(trucks))
                cities = list(range(cities))
                tclist = zerolistmaker(len(trucks))
                cclist = [None]* ccNb
                for i in range(ccNb):
                        cclist[i] = generateRandom(0,len(cities)-1)
                cclist = random.sample(range(len(cities)), ccNb)
                for i in range(tcNb):
                        ran = generateRandom(0,len(trucks)-1)
                        tclist[ran] = 1
                return trucksM, trucks, cities, cclist, tclist

        @staticmethod
        def generateHA(trucks, cities):
                np.random.seed(0)
                trucksM = np.random.randint(50,1500, size=(trucks, cities))
                trucksM = trucksM.tolist()
                return trucksM

        @staticmethod
        def generateSRSCC(trucks, cities, tcNb, ccNb):
                np.random.seed(0)
                trucksM = np.random.randint(50,1500, size=(trucks, cities))
                trucksM = trucksM.tolist()

                def zerolistmaker(n):
                        listofzeros = [0] * n
                        return listofzeros

                def generateRandom(start,end):
                        ran = random.randint(start, end)
                        return ran

                np.random.seed(0)

                trucks = list(range(trucks))
                cities = list(range(cities))
                tclist = zerolistmaker(len(trucks))
                cclist = [None]* ccNb
                for i in range(ccNb):
                        cclist[i] = generateRandom(0,len(cities)-1)
                cclist = random.sample(range(len(cities)), ccNb)
                for i in range(tcNb):
                        ran = generateRandom(0,len(trucks)-1)
                        tclist[ran] = 1

                return trucksM, cclist, tclist


#Generator.generateSRSCC(6,30,2,4)


#m = str(m)


#m = re.sub("\s+", ",", m)
#m = m.tolist()
#print(m.tolist())



#trucksM = str(trucksM)
#trucksM = re.sub("\s+", ",", trucksM)

'''
                trucksM = [[999, 454, 317, 165, 528, 222, 223, 410],
                           [453, 999, 253, 291, 210, 325, 234, 121],
                           [317, 252, 999, 202, 226, 108, 158, 140],
                           [165, 292, 201, 999, 344, 94, 124, 248],
                           [508, 210, 235, 346, 999, 336, 303, 94],
                           [222, 325, 116, 93, 340, 999, 182, 247],
                           [223, 235, 158, 125, 302, 185, 999, 206]]
                trucks = list(range(6))
                cities = list(range(6))
'''