import random
import math
def set_nature():
    while True:
        target_string = input("Enter target string: ")
        target = list(target_string)
        population = 1000
        # extent of mutation in range 1 to 100
        mutation_extent = 3
        population_record = generate_random_population(len(target), population)
        generation = 0
        while True:
            natural_selection_probability = calculate_score(population_record, target)
            population_record = perform_natural_selection(population_record, natural_selection_probability, mutation_extent)
            fittest = natural_selection_probability.index(max(natural_selection_probability))
            str = ""
            for genes in population_record[fittest]:
                str += genes
            print(str)
            generation += 1
            # print("score: ", natural_selection_probability[fittest])
            if str == target_string:
                print(generation, "Generations")
                print("\n**** Mother String mutation completed ****\n")
                break

def generate_random_population(no_of_genes, population):
    population_record = []
    for i in range(0,population):
        temp_dna = []
        for j in range(0,no_of_genes):
            temp_dna.append(chr(random.randint(32,126)))
        population_record.append(temp_dna)
        del(temp_dna)
    return population_record

def calculate_score(population_record, target):
    selection_probability = []
    for dna in population_record:
        score = 0
        for gene in range(0, len(target)):
            if dna[gene]== target[gene]:
                score+=1
        selection_probability.append(pow((score/len(target)*100), 4))
    return selection_probability 

def perform_natural_selection(population_record, selection_prob, mutation_extent):
    population = len(population_record)
    next_generation = []
    for i in range(0, population):
        parents = random.choices(population_record, weights=selection_prob, k=2)
        child = crossover(parents, mutation_extent)
        next_generation.append(child)
    return next_generation    
        
def crossover(parents, mutation_extent):
    infant = []
    parentA = parents[0]
    parentB = parents[1]
    midpoint = random.randint(0,len(parentA))
    for i in range(0,midpoint):
        infant.append(parentA[i])
    for i in range(midpoint, len(parentA)):
        infant.append(parentB[i])
    child = mutation(infant, mutation_extent)
    return child

def mutation(infant, mutation_extent):
    chances = list(range(mutation_extent))
    genes_modify = math.floor(len(infant)*mutation_extent/100)
    if genes_modify == 0: 
        genes_modify+=1 
    if random.randint(0,100) in chances:
        for i in range(genes_modify):
            infant[random.randint(0,len(infant)-1)] = chr(random.randint(32,126))
    return infant        

set_nature()    
 
