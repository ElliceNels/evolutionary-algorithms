import json
from pathlib import Path

from genetic_algorithm import Chromosome, GeneticAlgorithm
from config import Config

def load_config(file_path: str | Path) -> Config:
    with open(file_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    return Config(**config_data)


def format_chromosome(chromosome: Chromosome) -> str:
    return "(" + ", ".join(f"{gene:.4f}" for gene in chromosome) + ")"


def main():
    config = load_config("config.json")

    ga = GeneticAlgorithm(
        config.crossover_rate,
        config.mutation_rate,
        config.number_of_offspring,
        config.population_size,
        config.crossover_signal,
        config.chromosome_length,
        mutation_step=config.mutation_step,
        seed=config.seed,
        optimum_fitness=config.optimum_fitness,
        target_error=config.target_error,
        lower_bound=config.lower_bound,
        upper_bound=config.upper_bound,
        evaluation_budget=config.evaluation_budget,
    )

    print("Initial population:")
    for chromosome in ga.get_population():
        print(format_chromosome(chromosome))
    print()

    best_individuals = ga.run_evolution()
    print()

    print("Best across all evaluations:")
    for chromosome, fitness in best_individuals.items():
        print(f"{format_chromosome(chromosome)}  fitness = {fitness:.4e}, error = {ga.get_error(fitness):.4e}")

    print(f"Objective evaluations: {ga.evaluations}")
    if ga.first_target_evaluation is None:
        print("Target error was not reached.")
    else:
        print(f"Target error first reached at evaluation {ga.first_target_evaluation}.")
    print()

    print("Final population:")
    for chromosome in ga.get_population():
        print(format_chromosome(chromosome))

if __name__ == "__main__":
    main()
