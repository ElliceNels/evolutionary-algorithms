import random


Chromosome = tuple[float, ...]
LOWER_BOUND = -1.0
UPPER_BOUND = 1.0

class GeneticAlgorithm:
    """
    A class to represent a genetic algorithm.
    """

    def __init__(
        self,
        crossover_rate: float,
        mutation_rate: float,
        number_of_offspring: int,
        population_size: int,
        crossover_signal: int,
        chromosome_length: int,
        mutation_step: float,
    ):
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.mutation_step = mutation_step
        self.number_of_offspring = number_of_offspring
        self.population_size = population_size
        self.crossover_signal = crossover_signal
        self.chromosome_length = chromosome_length
        self.current_population = []
        self._initialise_population()

    def _initialise_population(self, seed=None):
        """
        Initialise the population with random individuals.

        Args:
            seed (int, optional): The seed for the random number generator. Defaults to None.
        """

        if seed is not None:
            random.seed(seed)

        self.current_population = []

        for _ in range(self.population_size):
            chromosome = tuple(
                random.uniform(LOWER_BOUND, UPPER_BOUND)
                for _ in range(self.chromosome_length)
            )
            self.current_population.append(chromosome)

    def _select_parent(self, population):
        """Select a parent from the population using tournament selection."""

        individual1, individual2 = random.sample(population, 2)

        if self._check_fitness(individual1) <= self._check_fitness(individual2):
            return individual1

        return individual2

    def _apply_crossover(self, individual1: Chromosome, individual2: Chromosome) -> list[Chromosome]:
        """Apply crossover or reproduction to two individuals to produce offspring.

        Args:
            individual1 (Chromosome): The first individual.
            individual2 (Chromosome): The second individual.

        Returns:
            list[Chromosome]: A list of the offspring produced by crossover or reproduction.
        """

        # Decide whether crossover occurs
        if random.random() >= self.crossover_rate:
            # The parent tuples are immutable.
            return [individual1, individual2]

        # Use the configured crossover point
        point = self.crossover_signal

        #Create two offspring
        offspring1 = individual1[:point] + individual2[point:]
        offspring2 = individual2[:point] + individual1[point:]

        return [offspring1, offspring2]

    def _apply_mutation(self, individual: Chromosome) -> Chromosome:
        """Perturb each selected gene by a bounded uniform offset."""
        mutated_individual = []

        for gene in individual:
            if random.random() < self.mutation_rate:
                gene += random.uniform(-self.mutation_step, self.mutation_step)
                gene = min(UPPER_BOUND, max(LOWER_BOUND, gene))
            mutated_individual.append(gene)

        return tuple(mutated_individual)

    def _check_fitness(self, individual: Chromosome) -> float:
        """Calculate the sum of squared genes, with a minimum at zero."""
        return sum(gene ** 2 for gene in individual)

    def _generate_new_population(self, population):
        """Perform selection, crossover, and mutation to generate a new population.

        Args:
            population (list[Chromosome]): The current population of individuals.

        Returns:
            list[Chromosome]: The new population of individuals after selection, crossover, and mutation.
        """

        working_population = []

        while len(working_population) < self.population_size:
            # Select two parents
            parent1 = self._select_parent(population)
            parent2 = self._select_parent(population)

            # Apply crossover or reproduction
            offsprings = self._apply_crossover(parent1, parent2)

            # Apply mutation to offspring
            for offspring in offsprings[:self.number_of_offspring]:

                mutated_offspring = self._apply_mutation(offspring)

                # Add to the new population
                working_population.append(mutated_offspring)

                # Stop if population is full
                if len(working_population) >= self.population_size:
                    break

        return working_population

    def run_evolution(self, iterations):
        """Run the evolution process for a specified number of iterations.

        Args:
            iterations (int): The number of iterations to run the evolution process.

        Returns:
            dict[Chromosome, float]: A dictionary containing the best individuals and their fitness scores.
        """

        for generation in range(iterations):

            # Get the best individuals from the current population
            best_individuals = self.get_best_individuals()
            best_fitness = min(best_individuals.values())

            print(f"Generation {generation}: Best fitness this generation = {best_fitness:.4f}")

            # Stop if optimal solution found
            if best_fitness == 0.0:
                print("Optimal solution found!")
                break

            self.current_population = self._generate_new_population(
                self.current_population
            )

        return self.get_best_individuals()

    def get_population(self):
        return self.current_population

    def get_best_individuals(self, population=None) -> dict[Chromosome, float]:
        """Get the best individuals from the population."""

        if population is None:
            population = self.current_population

        best_fitness = min(
            self._check_fitness(individual)
            for individual in population
        )

        best_individuals = {}

        for individual in population:
            if self._check_fitness(individual) == best_fitness:
                best_individuals[individual] = best_fitness

        return best_individuals
