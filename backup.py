
#cities = {0: 'c0', 1: 'c1', 2: 'c2', 3: 'c3', 4: 'c4', 5: 'c5', 6: 'c6', 7: 'c7',8:'8',9:'9',10:'10',11:'11',12:'12',13:'13',14:'14',15:'15',16:'16',17:'17',18:'18',19:'19',20:'20',21:'21',22:'22',23:'23'}
cities = [0,1,2,3,4,5,6,7]
# Distance between each pair of cities
'''
t0 = [999, 454, 317, 165, 528, 222, 223, 410,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]
t1 = [453, 999, 253, 291, 210, 325, 234, 121,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]
t2 = [317, 252, 999, 202, 226, 108, 158, 140,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]
t3 = [165, 292, 201, 999, 344, 94, 124, 248,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]
t4 = [508, 210, 235, 346, 999, 336, 303, 94,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]
t5 = [222, 325, 116, 93, 340, 999, 182, 247,999, 454, 317, 165, 528, 222, 223, 410,453, 999, 253, 291, 210, 325, 234, 121]

'''
t0 = [999, 454, 317, 165, 528, 222, 223, 410]
t1 = [453, 999, 253, 291, 210, 325, 234, 121]
t2 = [317, 252, 999, 202, 226, 108, 158, 140]
t3 = [165, 292, 201, 999, 344, 94, 124, 248]
t4 = [508, 210, 235, 346, 999, 336, 303, 94]
t5 = [222, 325, 116, 93, 340, 999, 182, 247]




trucksM = [[999, 454, 317, 165, 528, 222, 223, 410],
      [453, 999, 253, 291, 210, 325, 234, 121],
      [317, 252, 999, 202, 226, 108, 158, 140],
      [165, 292, 201, 999, 344, 94, 124, 248],
      [508, 210, 235, 346, 999, 336, 303, 94],
      [222, 325, 116, 93, 340, 999, 182, 247],
      [223, 235, 158, 125, 302, 185, 999, 206]]




#trucks = {0: t0, 1: t1, 2: t2, 3: t3, 4: t4, 5: t5}
trucks = [0,1,2,3,4,5]

'''
 countInn = count1
 #this will give an error, it needs to be swapped
 while copy_child1[countInn+1] in cc:
     countInn+=1
     print('infinite loop 1')
 #child1[count1], child1[countInn] = child1[countInn], child1[count1]
 diff = Diff(self.genes,copy_child1+cc)
 random.shuffle(diff)
 child1[count1] = diff[0]
 '''


def swap_random(chromosome):
      # idx = range(len(chromosome))
      # i1, i2 = random.sample(idx, 2)
      # while  tc[i1]==1 and chromosome[i2] in cc or tc[i2] and chromosome[i1] in cc:
      # i1, i2 = random.sample(idx, 2)

      new_list = [el for el in chromosome if el not in cc]
      if len(new_list) == 1:
            new_list = [el for el in self.genes if el not in cc]
            i1, i2 = random.sample(new_list, 2)
            idx = range(len(chromosome))
            idx1, idx2 = random.sample(idx, 2)
            chromosome[idx1] = i1
            chromosome[idx2] = i2
      else:
            print('new_list')
            print(new_list)
            i1, i2 = random.sample(new_list, 2)
            i1 = chromosome.index(i1)
            i2 = chromosome.index(i2)
            chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]

      # chromosome[i1], chromosome[i2] = chromosome[i2], chromosome[i1]
      return chromosome