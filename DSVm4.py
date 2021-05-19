import random
from random import randrange
from time import time
import numpy as np
import matplotlib.pyplot as plt
from generator import Generator




class Problem_Genetic(object):
    # =====================================================================================================================================
    # Class to represent problems to be solved by means of a general
    # genetic algorithm. It includes the following attributes:
    # - genes: list of possible genes in a chromosome
    # - individuals_length: length of each chromosome
    # - decode: method that receives the genotype (chromosome) as input and returns
    #    the phenotype (solution to the original problem represented by the chromosome)
    # - fitness: method that returns the evaluation of a chromosome (acts over the
    #    genotype)
    # - mutation: function that implements a mutation over a chromosome
    # - crossover: function that implements the crossover operator over two chromosomes
    # =====================================================================================================================================

    def __init__(self, genes, trucknb, individuals_length, decode, fitness):
        self.genes = genes
        self.individuals_length = individuals_length
        self.decode = decode
        self.fitness = fitness
        self.trucknb = trucknb


    def mutation(self, chromosome, prob):

        def Diff(li1, li2):
            return (list(list(set(li1) - set(li2)) + list(set(li2) - set(li1))))

        def replace_one_randomM4(chromosome_aux):
            chromosome = chromosome_aux
            i1 = random.choice(range(len(chromosome)))
            temp = chromosome[i1]
            temp = Diff(self.genes,chromosome)
            chromosome[i1] = random.choice(temp)
            return chromosome


        aux = []
        for _ in range(len(chromosome)):
            if random.random() < prob:
                aux = replace_one_randomM4(chromosome)
        return aux

    def crossover(self, parent1, parent2):

        def process_gen_repeated(copy_child1, copy_child2):
            count1 = 0
            # this checks if there are two the same elements in the copy_child1
            for gen1 in copy_child1[:pos]:
                repeat = 0
                repeat = copy_child1.count(gen1)
                if repeat > 1:  # If need to fix repeated gen
                    count2 = 0
                    # parent1[pos:] has the remaining elements that could be choosen
                    for gen2 in parent1[pos:]:  # Choose next available gen
                        ##if the element from the parent1 is not in child1 it means that instead of this element another element got reapeated
                        if gen2 not in copy_child1:
                            # here this replaces the repeated element (gen1) with the gen2 that is not in copy_child1
                            # if gen2 is in the copy_child1 then it adds the counter and will replace another element
                            child1[count1] = parent1[pos:][count2]
                        count2 += 1
                count1 += 1

            count1 = 0
            for gen1 in copy_child2[:pos]:
                repeat = 0
                repeat = copy_child2.count(gen1)
                if repeat > 1:  # If need to fix repeated gen
                    count2 = 0
                    for gen2 in parent2[pos:]:  # Choose next available gen
                        if gen2 not in copy_child2:
                            child2[count1] = parent2[pos:][count2]
                        count2 += 1
                count1 += 1

            return [child1, child2]

        pos = random.randrange(1, self.trucknb - 1)
        child1 = parent1[:pos] + parent2[pos:]
        child2 = parent2[:pos] + parent1[pos:]

        return process_gen_repeated(child1, child2)


class DSVm4:

    def __init__(self, trucks, cities):
        self.trucksM, self.trucks, self.cities = Generator.generateGA(trucks, cities)
        self.results = []

    def decodeTSP(self, chromosome):
        lista = []
        for i in chromosome:
            lista.append(self.cities[i])
        return lista

    def penalty(self, chromosome):
        actual = chromosome
        value_penalty = 0
        for i in actual:
            times = 0
            times = actual.count(i)
            if times > 1:
                value_penalty += 1000 * abs(times - len(actual))
        return value_penalty

    def fitnessTSP(self, chromosome):
        def distanceTrip(index, city):
            w = self.trucksM[index]
            return w[city]

        actualChromosome = list(chromosome)

        fitness_value = 0
        count = 0

        # Penalty for a city repetition inside the chromosome
        penalty_value = self.penalty(actualChromosome)

        for i in range(len(actualChromosome)):
            fitness_value += distanceTrip(i, chromosome[i]) + 50 * penalty_value
            count += 1
        return fitness_value

    def genetic_algorithm_t(self, Problem_Genetic, k, opt, ngen, size, ratio_cross, prob_mutate):
        def initial_population(Problem_Genetic, size):
            trucks = Problem_Genetic.trucknb

            def generate_chromosome():
                chromosome = []
                for i in Problem_Genetic.genes:
                    chromosome.append(i)

                chromosome = random.sample(chromosome, trucks)

                random.shuffle(chromosome)
                return chromosome

            return [generate_chromosome() for _ in range(size)]

        def new_generation_t(Problem_Genetic, k, opt, population, n_parents, n_directs, prob_mutate):

            # choses the best 20 chromosomes based on a random sampling
            def tournament_selection(Problem_Genetic, population, n, k, opt):
                winners = []

                for _ in range(int(n)):
                    elements = random.sample(population, k)
                    winners.append(opt(elements, key=Problem_Genetic.fitness))
                return winners

            def cross_parents(Problem_Genetic, parents):
                childs = []
                # range(start, stop, step)
                # the below extends by two chromosomes
                for i in range(0, len(parents), 2):
                    childs.extend(Problem_Genetic.crossover(parents[i], parents[i + 1]))
                return childs

            def mutate(Problem_Genetic, population, prob):
                for i in population:
                    Problem_Genetic.mutation(i, prob)
                return population

            # directs gives 20 'winning' chromosomes
            directs = tournament_selection(Problem_Genetic, population, n_directs, k, opt)
            # crosses takes the tournament selection output of size 80 as this si the nb of parents
            crosses = cross_parents(Problem_Genetic,
                                    tournament_selection(Problem_Genetic, population, n_parents, k, opt))
            mutations = mutate(Problem_Genetic, crosses, prob_mutate)
            new_generation = directs + mutations

            return new_generation

        population = initial_population(Problem_Genetic, size)
        n_parents = round(size * ratio_cross)
        n_parents = (n_parents if n_parents % 2 == 0 else n_parents - 1)
        n_directs = int(size - n_parents)
        inncount = 0
        for _ in range(ngen):
            inncount+=1

            population = new_generation_t(Problem_Genetic, k, opt, population, n_parents, n_directs, prob_mutate)
            bestChrom = opt(population, key=Problem_Genetic.fitness)

            fit = Problem_Genetic.fitness(bestChrom)

            self.results.append(fit)

        def allocation(genotype):
            lista = []
            for i in range(len(genotype)):
                arg = str('truck ' + str(i) + '---> customer ' + str(genotype[i]))
                lista.append(arg)
            return lista

        bestChromosome = opt(population, key=Problem_Genetic.fitness)
        # print("Chromosome: ", bestChromosome)
        genotype = Problem_Genetic.decode(bestChromosome)
        print("Solution:", (allocation(genotype), Problem_Genetic.fitness(bestChromosome)))
        print("Total allocation cost:", Problem_Genetic.fitness(bestChromosome))
        return (genotype, Problem_Genetic.fitness(bestChromosome))

    # ========================================================================THIRD PART: EXPERIMENTATION=========================================================
    # Run over the same instances both the standard GA (from first part) as well as the modified version (from second part).
    # Compare the quality of their results and their performance. Due to the inherent randomness of GA,
    # the experiments performed over each instance should be run several times.
    # ============================================================================================================================================================

    def run(self, k, printRate):
        DSV_PROBLEM = Problem_Genetic(self.cities, len(self.trucks), len(self.cities), lambda x: self.decodeTSP(x),
                                      lambda y: self.fitnessTSP(y))

        arrTime = []

        print(
                "--------------------------------------------------------- Genetic Algorithm M4 --------------------------------------------------------- \n")
        tiempo_inicial_t2 = time()
        cont = 1
        while cont <= k:
            v2 = len(self.trucks) * 10
            v1 = v2 * 2
            # k=
            # opt=
            # ngen = nb of generations
            # size = nb of chrimosome in the initial population
            self.genetic_algorithm_t(DSV_PROBLEM, 2, min, v1, v2, 0.5, 0.05)
            # genetic_algorithm_t(self, Problem_Genetic, k, opt, ngen, size, ratio_cross, prob_mutate):
            cont += 1
        tiempo_final_t2 = time()
        total_time = tiempo_final_t2 - tiempo_inicial_t2
        arrTime.append(total_time)
        print("Total time: ", total_time, " secs.\n")



        if printRate:
            plt.plot(self.results)
            plt.show()

        return self.results, arrTime


DSVproblem = DSVm4(10,15)
DSVproblem.run(10,True)


'''
if __name__ == "__main__":
    # Constant that is an instance object
    genetic_problem_instances = 10
    print("EXECUTING ", genetic_problem_instances, " INSTANCES \n")
    DSV(genetic_problem_instances)
    '''

