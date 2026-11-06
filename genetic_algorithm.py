import random

class GeneticAlgorithm:

    def __init__(self, crossover_rate, mutation_rate, number_of_offspring, population_size, crossover_signal, chromosome_length):
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.number_of_offspring = number_of_offspring
        self.population_size = population_size
        self.crossover_signal = crossover_signal
        self.chromosome_length = chromosome_length
        self.current_population = []
        self._initialise_population()

    def _initialise_population(self, seed=None):
        if seed is not None:
            random.seed(seed)

        self.current_population = []

        for _ in range(self.population_size):
            chromosome = ""

            for _ in range(self.chromosome_length):
                bit = random.choice(["0", "1"])
                chromosome += bit

            self.current_population.append(chromosome)

    def _select_parent(self, population):
        individual1, individual2 = random.sample(population, 2)

        if self._check_fitness(individual1) >= self._check_fitness(individual2):
            return individual1

        return individual2

    def _apply_crossover(self, individual1, individual2) -> list[str]:

        # Decide whether crossover occurs
        if random.random() >= self.crossover_rate:
            # Reproduction: return copies of the parents
            return [individual1, individual2]

        # Use the configured crossover point
        point = self.crossover_signal

        #Create two offspring
        offspring1 = individual1[:point] + individual2[point:]
        offspring2 = individual2[:point] + individual1[point:]

        return [offspring1, offspring2]

    def _apply_mutation(self, individual) -> str:
        mutated_individual = ""

        for bit in individual:
            if random.random() < self.mutation_rate:
                if bit == "0":
                    mutated_individual += "1"
                else:
                    mutated_individual += "0"
            else:
                mutated_individual += bit

        return mutated_individual

    def _check_fitness(self, individual) -> int:
        fitness_score = individual.count("0")
        return fitness_score

    def _generate_new_population(self, population):
        working_population = []

        while len(working_population) < self.population_size:

            #Select two parents
            parent1 = self._select_parent(population)
            parent2 = self._select_parent(population)

            #Apply crossover or reproduction
            offsprings = self._apply_crossover(parent1, parent2)

            #Apply mutation to offspring
            for offspring in offsprings[:self.number_of_offspring]:

                mutated_offspring = self._apply_mutation(offspring)

                #Add to the new population
                working_population.append(mutated_offspring)

                #Stop if population is full
                if len(working_population) >= self.population_size:
                    break

        return working_population

    def run_evolution(self, iterations):

        for generation in range(iterations):

            best_individuals = self.get_best_individuals()
            best_fitness = max(best_individuals.values())

            print(f"Generation {generation}: Best fitness = {best_fitness}")

            # Stop if optimal solution found
            if best_fitness == self.chromosome_length:
                print("Optimal solution found!")
                break

            self.current_population = self._generate_new_population(
                self.current_population
            )

        return self.get_best_individuals()

    def get_population(self):
        return self.current_population

    def get_best_individuals(self, population=None) -> dict[str, int]:

        if population is None:
            population = self.current_population

        best_fitness = max(
            self._check_fitness(individual)
            for individual in population
        )

        best_individuals = {}

        for individual in population:
            if self._check_fitness(individual) == best_fitness:
                best_individuals[individual] = best_fitness

        return best_individuals
