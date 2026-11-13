import operator
from copy import deepcopy
import random
from anytree import Node

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda left, right: left / right if right != 0 else 0,
}
OPERANDS = ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5", "x"]

class GeneticAlgorithm:
    """
    A class to represent a genetic algorithm.
    """

    def __init__(self, crossover_rate, mutation_rate, population_size, max_depth, target_lookup, seed=None):
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.current_population = []
        self.max_depth = max_depth
        self.target_lookup = target_lookup
        self.seed = seed
        self._initialise_population()

    def _initialise_population(self):
        """
        Initialise the population with random individuals.

        Args:
            seed (int, optional): The seed for the random number generator. Defaults to None.
        """

        if self.seed is not None:
            random.seed(self.seed)

        self.current_population = []

        for _ in range(self.population_size):
            self.current_population.append(self._new_individual())

    def _new_individual(self, depth=0):
        """Generate a new random individual/tree ().

        Returns:
            Node: A new random individual (tree).
        """
        if depth >= self.max_depth:
            # Return a terminal node (leaf node) with a random value
            return Node(random.choice(OPERANDS))
        else:
            # Return a non-terminal node (operators)
            root = Node(random.choice(tuple(OPERATIONS)))

            left =  self._new_individual(depth + 1)
            right = self._new_individual(depth + 1)

            left.parent = root
            right.parent = root

            return root


    def _select_parent(self, population):
        """Select a parent from the population using tournament selection."""

        individual1, individual2 = random.sample(population, 2)

        if self._check_fitness(individual1) >= self._check_fitness(individual2):
            return individual1

        return individual2

    def _apply_crossover(self, individual1: Node, individual2: Node) -> list[Node]:
        """Apply crossover or reproduction to two individuals to produce offspring.

        Args:
            individual1 (Node): The first individual.
            individual2 (Node): The second individual.

        Returns:
            list[Node]: A list of the offspring produced by crossover or reproduction.
        """
        offspring1 = deepcopy(individual1)
        offspring2 = deepcopy(individual2)

        # Decide whether crossover occurs
        if random.random() >= self.crossover_rate:
            # Reproduction: return copies of the parents
            return [offspring1, offspring2]


        # Use randomly selected crossover point to create offspring
        crossover_node1: Node = random.choice(list(offspring1.descendants) + [offspring1])
        crossover_node2: Node = random.choice(list(offspring2.descendants) + [offspring2])
        # Create two offspring by swapping subtrees at the crossover nodes
        crossover_node1_parent = crossover_node1.parent
        crossover_node2_parent = crossover_node2.parent

        crossover_node1.parent = None
        crossover_node2.parent = None
        crossover_node1.parent = crossover_node2_parent
        crossover_node2.parent = crossover_node1_parent

        return [offspring1, offspring2]

    def _apply_mutation(self, individual: Node) -> Node:
        """Apply mutation to an individual by flipping bits with a certain probability.

        Args:
            individual (Node): The individual to mutate.

        Returns:
            Node: The mutated individual.
        """

        if not (random.random() < self.mutation_rate):
            return individual

        # Copy the individual to avoid modifying the original
        mutated_individual = deepcopy(individual)

        node_to_mutate: Node = (random.choice(list(mutated_individual.descendants)))
        if node_to_mutate.is_leaf:
            # get all leaf nodes
            node_to_mutate.name = random.choice(OPERANDS)
        else:
            # get all non-leaf nodes
            node_to_mutate.name = random.choice(list(OPERATIONS.keys()))

        return mutated_individual


    def _evaluate_individual(self, individual, x) -> int:
        """Evaluate the fitness of an individual.

        Args:
            individual (Node): The root node of the individual to evaluate.

        Returns:
            int: The fitness score of the individual.
        """

        # Evaluate the individual using a depth-first traversal of the tree
        def evaluate_node(node: Node) -> int | float:
            if node.is_leaf:
                if node.name == "x":
                    return x
                return int(node.name)

            left, right = node.children
            left_value = evaluate_node(left)
            right_value = evaluate_node(right)

            return OPERATIONS[node.name](left_value, right_value)

        return evaluate_node(individual)

    def _check_fitness(self, individual) -> int:
        """Calculate the fitness score of an individual."""

        error = 0

        x_values = self.target_lookup.keys()
        for x in x_values:
            prediction = self._evaluate_individual(individual, x)  # Example evaluation with x=1
            target = self.target_lookup[x]
            mse = (abs(prediction - target) ** 2) / len(x_values)
            error += mse
        return 1 / (1 + error)  # Fitness is inversely related to error

    def _generate_new_population(self, population):
        """Perform selection, crossover, and mutation to generate a new population.

        Args:
            population (list[str]): The current population of individuals.

        Returns:
            list[str]: The new population of individuals after selection, crossover, and mutation.
        """

        working_population = []

        while len(working_population) < self.population_size:
            # Select two parents
            parent1 = self._select_parent(population)
            parent2 = self._select_parent(population)

            # Apply crossover or reproduction
            offsprings = self._apply_crossover(parent1, parent2)

            # Apply mutation to offspring
            for offspring in offsprings:
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
            dict[str, Node]: A dictionary containing the best individuals and their fitness scores.
        """

        for generation in range(iterations):

            # Get the best individuals from the current population
            best_individuals = self.get_best_individuals()
            best_fitness = max(best_individuals.values())

            print(f"Generation {generation}: Best fitness = {best_fitness}")

            # Stop if optimal solution found
            if best_fitness == 1.0:
                print("Optimal solution found!")
                break

            self.current_population = self._generate_new_population(
                self.current_population
            )

        return self.get_best_individuals()

    def get_population(self):
        return self.current_population

    def get_best_individuals(self, population=None) -> dict[str, Node]:
        """Get the best individuals from the population."""

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


    def display_tree(self, root: Node):
        """Display the tree structure of an individual using anytree.

        Args:
            root (Node): The root node of the tree to display.
        """
        from anytree import RenderTree

        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")