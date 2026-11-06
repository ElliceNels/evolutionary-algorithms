import json
from pathlib import Path

from genetic_algorithm import GeneticAlgorithm
from config import Config

def load_config(file_path: str | Path) -> Config:
    with open(file_path, "r") as file:
        config_data = json.load(file)

    return Config(**config_data)

def main():
    config = load_config("config.json")

    ga = GeneticAlgorithm(
        config.crossover_rate,
        config.mutation_rate,
        config.number_of_offspring,
        config.population_size,
        config.crossover_signal,
        config.chromosome_length
    )

    print(f"Initial population:\n{ga.get_population()}")
    print(f"Final population:\n{ga.get_population()}")
    print(f"Best individuals:\n{ga.run_evolution(config.iterations)}")

if __name__ == "__main__":
    main()
