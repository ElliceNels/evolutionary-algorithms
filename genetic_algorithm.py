class GeneticAlgorithm:

    def __init__(self, crossover_rate, mutation_rate, number_of_offspring, population_size, crossover_signal):
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.number_of_offspring = number_of_offspring
        self.population_size = population_size
        self.crossover_signal = crossover_signal
        self.current_population = ["101010", "101010"]
        self.current_population = {"101010": 4, "101010": 3}
        self._initialise_population()

    def _initialise_population(self, seed):
        self.current_population = ["" * self.population_size]
        # get fitness bases

    def _apply_crossover(self, individual1, individual2) -> list[str]:
        self.crossover_rate, self.crossover_rate
        offsprings = []
        return offsprings

    def _apply_mutation(self, individual) -> str:
        # randomly flip bit
        mutated_individual = individual
        return mutated_individual

    def _check_fitness(self, individual) -> int:
        fitness_score = 0
        return fitness_score

    def _generate_new_population(self, population):
        working_population = population
        for individual in self.current_population:
            # 1. applty crossover if needed / apply reproduction
            # 2. apply mutation
            ...
        return working_population

    def run_evolution(self, iterations):
        for _ in range(iterations):
            self.current_population = self._generate_new_population(self.current_population)

        return self.get_best_individuals(self.current_population)

    def get_population(self):
        return self.current_population

    def get_best_individuals(self, population) -> dict[str, int]:
        pass



crossover_rate = 0
mutation_rate = 0
number_of_offspring = 0
population_size = 0
crossover_signal = 0

ga = GeneticAlgorithm(crossover_rate, mutation_rate, number_of_offspring, population_size, crossover_signal)
ga.run_evolution()
final_pop = ga.get_population()
best_individuals = ga.get_best_individuals()

