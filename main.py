import json
from pathlib import Path

from genetic_algorithm import GeneticAlgorithm
from config import Config

def load_config(file_path: str | Path) -> Config:
    with open(file_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)

    return Config(**config_data)



def main():
    config = load_config("config.json")

    ga = GeneticAlgorithm(
        config.crossover_rate,
        config.mutation_rate,
        config.population_size,
        config.max_depth,
        config.target_lookup,
        config.seed
    )

    print(f"Initial population:\n{ga.get_population()}")
    print(f"Final population:\n{ga.get_population()}")
    resulting_best = ga.run_evolution(config.iterations)
    for best in resulting_best:
        print(f"Best individuals:\n{ga.display_tree(best)} with fitness: {resulting_best[best]}")

if __name__ == "__main__":
    main()
